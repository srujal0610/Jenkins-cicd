package com.stpl.training.message.bus.publisher;

public interface Publisher {

	public void publishAsyncEvent(String eventDestination, Object eventPayload);

}