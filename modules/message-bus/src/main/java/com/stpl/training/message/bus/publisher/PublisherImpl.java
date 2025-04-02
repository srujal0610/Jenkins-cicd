package com.stpl.training.message.bus.publisher;

import com.liferay.portal.kernel.log.Log;
import com.liferay.portal.kernel.log.LogFactoryUtil;
import com.liferay.portal.kernel.messaging.Message;
import com.liferay.portal.kernel.messaging.MessageBus;

import org.osgi.service.component.annotations.Component;
import org.osgi.service.component.annotations.Reference;

@Component(service = Publisher.class, immediate = true)
public class PublisherImpl implements Publisher {

	/**
	 * Publish async event.
	 *
	 * @param eventDestination event destination
	 * @param eventPayload     event payload
	 * @param serviceContext   the service context
	 */
	@Override
	public void publishAsyncEvent(String eventDestination, Object eventPayload) {

		try {

			for (int i = 1; i <= 20; i++) {
				Thread.sleep(180000);
				for (int j = 1; j <= 5; j++) {
					Message payloadMessage = new Message();
					int number = i * j;
					payloadMessage.setPayload(number);

					_messageBus.sendMessage(eventDestination, payloadMessage);
					_log.info("Successfully published message to destination : " + eventDestination);

				}
			}

		} catch (InterruptedException exception) {
			Thread.currentThread().interrupt();

			_log.error("while send the message");
		}

	}

	@Reference
	private MessageBus _messageBus;

	private static final Log _log = LogFactoryUtil.getLog(PublisherImpl.class);

}