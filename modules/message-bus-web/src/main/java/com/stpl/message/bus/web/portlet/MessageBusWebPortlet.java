package com.stpl.message.bus.web.portlet;

import com.liferay.portal.kernel.log.Log;
import com.liferay.portal.kernel.log.LogFactoryUtil;
import com.liferay.portal.kernel.portlet.bridges.mvc.MVCPortlet;
import com.stpl.message.bus.web.constants.MessageBusWebPortletKeys;
import com.stpl.training.message.bus.publisher.Publisher;

import java.io.IOException;

import javax.portlet.Portlet;
import javax.portlet.PortletException;
import javax.portlet.RenderRequest;
import javax.portlet.RenderResponse;

import org.osgi.service.component.annotations.Component;
import org.osgi.service.component.annotations.Reference;

@Component(
	immediate = true,
	property = {
		"com.liferay.portlet.display-category=category.sample",
		"com.liferay.portlet.header-portlet-css=/css/main.css",
		"com.liferay.portlet.instanceable=true",
		"javax.portlet.display-name=MessageBusWeb",
		"javax.portlet.init-param.template-path=/",
		"javax.portlet.init-param.view-template=/view.jsp",
		"javax.portlet.name=" + MessageBusWebPortletKeys.MESSAGEBUSWEB,
		"javax.portlet.resource-bundle=content.Language",
		"javax.portlet.security-role-ref=power-user,user"
	},
	service = Portlet.class
)
public class MessageBusWebPortlet extends MVCPortlet {

	@Override
	public void doView(RenderRequest renderRequest, RenderResponse renderResponse)
			throws IOException, PortletException {

		LOGGER.info("Message Bus web");
//		eventPublisher.publishAsyncEvent("message_bus", null);
		super.doView(renderRequest, renderResponse);
	}

	private static final Log LOGGER = LogFactoryUtil.getLog(MessageBusWebPortlet.class);

	@Reference
	private Publisher eventPublisher;

}