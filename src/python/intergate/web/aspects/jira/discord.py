from __future__ import annotations

from intergate.apis.discord.domain import Footer, Image
from intergate.apis.discord.pointcut import DiscordMessageClosure
from intergate.apis.jira.domain import JiraEvent
from intergate.types.alias import URL


class JiraAssets:
	LOGO_JIRA: URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLT_6JKK6ca5KZEg2BwsBXMZdggGvHEFFB3g&usqp=CAU"
	ICON_ATLASSIAN: URL = "https://symbols.getvecta.com/stencil_85/33_jira-icon.6a60be29f8.png"
	ICON_TASK: URL = "https://e7.pngegg.com/pngimages/441/504/png-clipart-jira-issue-tracking-system-atlassian-technical-support-computer-icons-consent-angle-text-thumbnail.png"


class JiraMessageClosure( DiscordMessageClosure[ JiraEvent ] ):

	def to_content( self, payload: JiraEvent ):
		return None

	def to_author( self, payload: JiraEvent ):
		return None

	def to_thumbnail( self, payload: JiraEvent ):
		return Image( url = JiraAssets.LOGO_JIRA )

	def to_field_list( self, payload: JiraEvent ):

		return [ 
						Field( name = "Creator:" , value = payload.fieldDict.creator.displayName),
						Field( name = "Relator:" , value = payload.fieldDict.relator.displayName)
				

		]

	def to_footer( self, payload: JiraEvent ):
		return Footer(
				text = f" [{payload.fieldDict.status.name}] {payload.key} ",
				icon_url = JiraAssets.ICON_ATLASSIAN
				)

	def to_title( self, payload: JiraEvent ):
		return f"{payload.fieldDict.project.name}"

	def to_url( self, payload: JiraEvent ):
		return None

	def to_color( self, payload: JiraEvent ):
		return None

	def to_description( self, payload: JiraEvent ):
		return None
