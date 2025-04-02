package com.stpl.training.message.bus.subscriber;

import com.liferay.portal.kernel.log.Log;
import com.liferay.portal.kernel.log.LogFactoryUtil;
import com.liferay.portal.kernel.messaging.Message;
import com.liferay.portal.kernel.messaging.MessageListener;
import com.liferay.portal.kernel.messaging.MessageListenerException;

import org.osgi.service.component.annotations.Component;


@Component(
	immediate = true,
	property = {
		"destination.name=message_bus"
	},
	service = MessageListener.class
)
public class Subscriber implements MessageListener{

	@Override
	public void receive(Message message) throws MessageListenerException {

		_log.info("message send: " + message.getPayload().toString());
	}

	private static final Log _log = LogFactoryUtil.getLog(Subscriber.class);

}
