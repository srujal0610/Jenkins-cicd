package com.stpl.training.message.bus.publisher;

import com.liferay.portal.kernel.log.Log;
import com.liferay.portal.kernel.log.LogFactoryUtil;
import com.liferay.portal.kernel.messaging.Destination;
import com.liferay.portal.kernel.messaging.DestinationConfiguration;
import com.liferay.portal.kernel.messaging.DestinationFactory;
import com.liferay.portal.kernel.util.HashMapDictionary;
import com.stpl.training.message.bus.constants.Constants;

import java.util.ArrayList;
import java.util.Dictionary;
import java.util.List;
import java.util.concurrent.RejectedExecutionHandler;
import java.util.concurrent.ThreadPoolExecutor;

import org.osgi.framework.BundleContext;
import org.osgi.framework.ServiceRegistration;
import org.osgi.service.component.annotations.Activate;
import org.osgi.service.component.annotations.Component;
import org.osgi.service.component.annotations.Deactivate;
import org.osgi.service.component.annotations.Reference;

@Component
public class DestinationActivator {

	@Activate
	public void activate(BundleContext bundleContext) {
		this.bundleContext = bundleContext;

		RejectedExecutionHandler rejectedExecutionHandler = new ThreadPoolExecutor.CallerRunsPolicy() {

			@Override
			public void rejectedExecution(Runnable runnable, ThreadPoolExecutor threadPoolExecutor) {
				if (_log.isWarnEnabled()) {
					_log.warn("The current thread will handle the request "
							+ "because the rules engine's task queue is at " + "its maximum capacity");
				}

				super.rejectedExecution(runnable, threadPoolExecutor);
			}

		};

		// Create a DestinationConfiguration for parallel destinations.

		DestinationConfiguration destinationConfiguration = DestinationConfiguration
				.createSerialDestinationConfiguration(Constants.DESTINATION_NAME);

		destinationConfiguration.setMaximumQueueSize(Constants.MAXIMUM_QUEUE_SIZE);
		destinationConfiguration.setWorkersCoreSize(Constants.WORKERS_CORE_SIZE);
		destinationConfiguration.setWorkersMaxSize(Constants.WORKERS_MAX_SIZE);
		destinationConfiguration.setRejectedExecutionHandler(rejectedExecutionHandler);

		// Create the destination

		Destination destination = destinationFactory.createDestination(destinationConfiguration);

		// Add the destination to the OSGi service registry

		Dictionary<String, Object> properties = new HashMapDictionary<>();
		properties.put("destination.name", destination.getName());

		destinationServiceRegistrationList
				.add(bundleContext.registerService(Destination.class, destination, properties));

		if (_log.isDebugEnabled()) {
			_log.debug("Successfully destination : " + Constants.DESTINATION_NAME + "- The destination name is : "
					+ Constants.DESTINATION_NAME);
		}

	}

	@Deactivate
	protected void deactivate() {

		// Unregister and destroy destinations this component unregistered

		if (_log.isDebugEnabled()) {
			_log.debug("Un-registering destination - STARTED");
		}

		for (ServiceRegistration<Destination> destinationServiceRegistration : destinationServiceRegistrationList) {
			if (destinationServiceRegistration != null) {
				Destination destination = bundleContext.getService(destinationServiceRegistration.getReference());

				if (_log.isDebugEnabled()) {
					_log.debug("Un-registering and destroying destination : " + destination.getName());
				}

				destinationServiceRegistration.unregister();
				destination.destroy();
			}
		}

		if (_log.isDebugEnabled()) {
			_log.debug("Un-registering destination - ENDED");
		}

		bundleContext = null;
	}

	@Reference
	private DestinationFactory destinationFactory;

	private volatile BundleContext bundleContext;

	private List<ServiceRegistration<Destination>> destinationServiceRegistrationList = new ArrayList<>();

	private static final Log _log = LogFactoryUtil.getLog(DestinationActivator.class);

}
