
from __future__ import annotations

import dataclasses as dc
import typing as t

from dubious.discord.disc import Snowflake

@dc.dataclass
class Interaction:
    id: Snowflake
    """  """

    application_id: Snowflake
    """  """

    type: InteractionType
    """  """

    data: InteractionData | None = dc.field(kw_only=True, default=None)
    """  """

    guild_id: Snowflake | None = dc.field(kw_only=True, default=None)
    """  """

    channel: PartialChannel | None = dc.field(kw_only=True, default=None)
    """  """

    channel_id: Snowflake | None = dc.field(kw_only=True, default=None)
    """  """

    member: GuildMember | None = dc.field(kw_only=True, default=None)
    """  """

    user: User | None = dc.field(kw_only=True, default=None)
    """  """

    token: str
    """  """

    version: int
    """  """

    message: Message | None = dc.field(kw_only=True, default=None)
    """  """

    app_permissions: str | None = dc.field(kw_only=True, default=None)
    """  """

    locale: str | None = dc.field(kw_only=True, default=None)
    """ `language` """

    guild_locale: str | None = dc.field(kw_only=True, default=None)
    """ `Guild's preferred locale` """

@dc.dataclass
class ApplicationCommandData:
    id: Snowflake
    """ ``ID`` """

    name: str
    """ ``name`` """

    type: int
    """ ``type`` """

    resolved: ResolvedData | None = dc.field(kw_only=True, default=None)
    """  """

    options: ApplicationCommandInteractionDataOptionlist[[application command interaction data option]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_INTERACTIONS_RECEIVING_AND_RESPONDING/interaction-object-application-command-interaction-data-option-structure)] """

    guild_id: Snowflake | None = dc.field(kw_only=True, default=None)
    """  """

    target_id: Snowflake | None = dc.field(kw_only=True, default=None)
    """ `user` """

@dc.dataclass
class MessageComponentData:
    custom_id: str
    """ ``custom_id`` """

    component_type: int
    """ `type` """

    values: SelectOptionValueslist[[select option values]( | None = dc.field(kw_only=True, default=None)
    """ `select menu`DOCS_INTERACTIONS_MESSAGE_COMPONENTS/select-menu-object-select-option-structure)] """

@dc.dataclass
class ModalSubmitData:
    custom_id: str
    """ ``custom_id`` """

    components: MessageComponentslist[[message components](
    """ DOCS_INTERACTIONS_MESSAGE_COMPONENTS/message-components)] """

@dc.dataclass
class ResolvedData:
    users: Userdict[Snowflake, [user]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_RESOURCES_USER/user-object) object] """

    members: PartialMemberdict[Snowflake, [partial member]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_RESOURCES_GUILD/guild-member-object) object] """

    roles: Roledict[Snowflake, [role]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_TOPICS_PERMISSIONS/role-object) object] """

    channels: PartialChanneldict[Snowflake, [partial channel]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_RESOURCES_CHANNEL/channel-object) object] """

    messages: PartialMessagesdict[Snowflake, [partial messages]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_RESOURCES_CHANNEL/message-object) object] """

    attachments: Attachmentdict[Snowflake, [attachment]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_RESOURCES_CHANNEL/attachment-object) object] """

@dc.dataclass
class ApplicationCommandInteractionDataOption:
    name: str
    """  """

    type: int
    """ `application command option type` """

    value: strintfloatbool | None = dc.field(kw_only=True, default=None)
    """  """

    options: ApplicationCommandInteractionDataOptionlist[[application command interaction data option]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_INTERACTIONS_RECEIVING_AND_RESPONDING/interaction-object-application-command-interaction-data-option-structure)] """

    focused: bool | None = dc.field(kw_only=True, default=None)
    """  """

@dc.dataclass
class MessageInteraction:
    id: Snowflake
    """  """

    type: InteractionType
    """  """

    name: str
    """ `application command` """

    user: UserObject
    """  """

    member: PartialMember | None = dc.field(kw_only=True, default=None)
    """  """

@dc.dataclass
class InteractionResponse:
    type: InteractionCallbackType
    """  """

    data: InteractionCallbackData | None = dc.field(kw_only=True, default=None)
    """  """

@dc.dataclass
class InteractionCallbackData:
    tts: bool | None = dc.field(kw_only=True, default=None)
    """  """

    content: str | None = dc.field(kw_only=True, default=None)
    """  """

    embeds: Embedslist[[embeds]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_RESOURCES_CHANNEL/embed-object)] """

    allowed_mentions: AllowedMentions | None = dc.field(kw_only=True, default=None)
    """ `allowed mentions` """

    flags: int | None = dc.field(kw_only=True, default=None)
    """ `message flags` """

    components: Componentslist[[components]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_INTERACTIONS_MESSAGE_COMPONENTS/)] """

    attachments: Attachmentlist[partial [attachment]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_RESOURCES_CHANNEL/attachment-object) object] """

@dc.dataclass
class Button:
    type: int
    """  """

    style: int
    """ `button style` """

    label: str | None = dc.field(kw_only=True, default=None)
    """  """

    emoji: Emoji | None = dc.field(kw_only=True, default=None)
    """  """

    custom_id: str | None = dc.field(kw_only=True, default=None)
    """  """

    url: str | None = dc.field(kw_only=True, default=None)
    """  """

    disabled: bool | None = dc.field(kw_only=True, default=None)
    """  """

@dc.dataclass
class SelectMenu:
    type: int
    """ `Type` """

    custom_id: str
    """  """

    options: SelectOptionslist[[select options]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_INTERACTIONS_MESSAGE_COMPONENTS/select-menu-object-select-option-structure)] """

    channel_types: ChannelTypeslist[[channel types]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_RESOURCES_CHANNEL/channel-object-channel-types)] """

    placeholder: str | None = dc.field(kw_only=True, default=None)
    """  """

    min_values: int | None = dc.field(kw_only=True, default=None)
    """  """

    max_values: int | None = dc.field(kw_only=True, default=None)
    """  """

    disabled: bool | None = dc.field(kw_only=True, default=None)
    """  """

@dc.dataclass
class SelectOption:
    label: str
    """  """

    value: str
    """  """

    description: str | None = dc.field(kw_only=True, default=None)
    """  """

    emoji: Emoji | None = dc.field(kw_only=True, default=None)
    """  """

    default: bool | None = dc.field(kw_only=True, default=None)
    """  """

@dc.dataclass
class TextInput:
    type: int
    """  """

    custom_id: str
    """  """

    style: int
    """ `Text Input Style` """

    label: str
    """  """

    min_length: int | None = dc.field(kw_only=True, default=None)
    """  """

    max_length: int | None = dc.field(kw_only=True, default=None)
    """  """

    required: bool | None = dc.field(kw_only=True, default=None)
    """  """

    value: str | None = dc.field(kw_only=True, default=None)
    """  """

    placeholder: str | None = dc.field(kw_only=True, default=None)
    """  """

@dc.dataclass
class ApplicationCommand:
    id: Snowflake
    """  """

    type: ApplicationCommandType | None = dc.field(kw_only=True, default=None)
    """ `Type of command` """

    application_id: Snowflake
    """  """

    guild_id: Snowflake | None = dc.field(kw_only=True, default=None)
    """  """

    name: str
    """ `Name of command` """

    name_localizations: dictionary with keys in [available locales]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_REFERENCE/locales) | NoneAvailableLocales """

    description: str
    """  """

    description_localizations: dictionary with keys in [available locales]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_REFERENCE/locales) | NoneAvailableLocales """

    options: ApplicationCommandOptionlist[[application command option]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_INTERACTIONS_APPLICATION_COMMANDS/application-command-object-application-command-option-structure)] """

    default_member_permissions: strstring | None
    """ `permissions` """

    dm_permission: bool | None = dc.field(kw_only=True, default=None)
    """  """

    default_permission: boolboolean | None = dc.field(kw_only=True, default=None)
    """  """

    nsfw: bool | None = dc.field(kw_only=True, default=None)
    """ `age-restricted` """

    version: Snowflake
    """  """

@dc.dataclass
class ApplicationCommandOption:
    type: ApplicationCommandOptionType
    """  """

    name: str
    """ `1-32 character name` """

    name_localizations: dictionary with keys in [available locales]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_REFERENCE/locales) | NoneAvailableLocales """

    description: str
    """  """

    description_localizations: dictionary with keys in [available locales]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_REFERENCE/locales) | NoneAvailableLocales """

    required: bool | None = dc.field(kw_only=True, default=None)
    """  """

    choices: ApplicationCommandOptionChoicelist[[application command option choice]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_INTERACTIONS_APPLICATION_COMMANDS/application-command-object-application-command-option-choice-structure)] """

    options: ApplicationCommandOptionlist[[application command option]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_INTERACTIONS_APPLICATION_COMMANDS/application-command-object-application-command-option-structure)] """

    channel_types: ChannelTypeslist[[channel types]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_RESOURCES_CHANNEL/channel-object-channel-types)] """

    min_value: intfloat | None = dc.field(kw_only=True, default=None)
    """  """

    max_value: intfloat | None = dc.field(kw_only=True, default=None)
    """  """

    min_length: int | None = dc.field(kw_only=True, default=None)
    """  """

    max_length: int | None = dc.field(kw_only=True, default=None)
    """  """

    autocomplete: bool | None = dc.field(kw_only=True, default=None)
    """  """

@dc.dataclass
class ApplicationCommandOptionChoice:
    name: str
    """  """

    name_localizations: dictionary with keys in [available locales]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_REFERENCE/locales) | NoneAvailableLocales """

    value: strintfloat
    """  """

@dc.dataclass
class GuildApplicationCommandPermissions:
    id: Snowflake
    """  """

    application_id: Snowflake
    """  """

    guild_id: Snowflake
    """  """

    permissions: ApplicationCommandPermissionslist[[application command permissions](
    """ DOCS_INTERACTIONS_APPLICATION_COMMANDS/application-command-permissions-object-application-command-permissions-structure)] """

@dc.dataclass
class ApplicationCommandPermissions:
    id: Snowflake
    """ `permission constant` """

    type: ApplicationCommandPermissionType
    """  """

    permission: bool
    """  """

@dc.dataclass
class StageInstance:
    id: Snowflake
    """  """

    guild_id: Snowflake
    """  """

    channel_id: Snowflake
    """  """

    topic: str
    """  """

    privacy_level: int
    """ `privacy level` """

    discoverable_disabled: bool
    """  """

    guild_scheduled_event_id: Snowflakesnowflake | None
    """  """

@dc.dataclass
class AutoModerationRule:
    id: Snowflake
    """  """

    guild_id: Snowflake
    """  """

    name: str
    """  """

    creator_id: Snowflake
    """  """

    event_type: int
    """ `event type` """

    trigger_type: int
    """ `trigger type` """

    trigger_metadata: 
    """ `trigger metadata` """

    actions: Actionlist[[action](
    """ DOCS_RESOURCES_AUTO_MODERATION/auto-moderation-action-object) object] """

    enabled: bool
    """  """

    exempt_roles: Snowflakelist[snowflake]
    """  """

    exempt_channels: Snowflakelist[snowflake]
    """  """

@dc.dataclass
class AutoModerationAction:
    type: ActionType
    """  """

    metadata: ActionMetadata | None = dc.field(kw_only=True, default=None)
    """  """

@dc.dataclass
class Emoji:
    id: Snowflakesnowflake | None
    """ `emoji id` """

    name: strstring (can be null only in reaction emoji objects) | None
    """  """

    roles: Rolelist[[role]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_TOPICS_PERMISSIONS/role-object) object id] """

    user: User | None = dc.field(kw_only=True, default=None)
    """  """

    require_colons: bool | None = dc.field(kw_only=True, default=None)
    """  """

    managed: bool | None = dc.field(kw_only=True, default=None)
    """  """

    animated: bool | None = dc.field(kw_only=True, default=None)
    """  """

    available: bool | None = dc.field(kw_only=True, default=None)
    """  """

@dc.dataclass
class Sticker:
    id: Snowflake
    """ `id of the sticker` """

    pack_id: Snowflake | None = dc.field(kw_only=True, default=None)
    """  """

    name: str
    """  """

    description: strstring | None
    """  """

    tags: str
    """  """

    asset: str | None = dc.field(kw_only=True, default=None)
    """  """

    type: int
    """ `type of sticker` """

    format_type: int
    """ `type of sticker format` """

    available: bool | None = dc.field(kw_only=True, default=None)
    """  """

    guild_id: Snowflake | None = dc.field(kw_only=True, default=None)
    """  """

    user: User | None = dc.field(kw_only=True, default=None)
    """  """

    sort_value: int | None = dc.field(kw_only=True, default=None)
    """  """

@dc.dataclass
class StickerItem:
    id: Snowflake
    """  """

    name: str
    """  """

    format_type: int
    """ `type of sticker format` """

@dc.dataclass
class StickerPack:
    id: Snowflake
    """  """

    stickers: Stickerlist[[sticker](
    """ DOCS_RESOURCES_STICKER/sticker-object) object] """

    name: str
    """  """

    sku_id: Snowflake
    """  """

    cover_sticker_id: Snowflake | None = dc.field(kw_only=True, default=None)
    """  """

    description: str
    """  """

    banner_asset_id: Snowflake | None = dc.field(kw_only=True, default=None)
    """ `banner image` """

@dc.dataclass
class Response:
@dc.dataclass
class AuditLog:
    application_commands: ApplicationCommandslist[[application commands](
    """ DOCS_INTERACTIONS_APPLICATION_COMMANDS/application-command-object) object] """

    audit_log_entries: AuditLogEntrylist[[audit log entry](
    """ DOCS_RESOURCES_AUDIT_LOG/audit-log-entry-object) object] """

    auto_moderation_rules: AutoModerationRulelist[[auto moderation rule](
    """ DOCS_RESOURCES_AUTO_MODERATION/auto-moderation-rule-object) object] """

    guild_scheduled_events: GuildScheduledEventlist[[guild scheduled event](
    """ DOCS_RESOURCES_GUILD_SCHEDULED_EVENT/guild-scheduled-event-object) object] """

    integrations: Integrationlist[partial [integration](
    """ DOCS_RESOURCES_GUILD/integration-object) object] """

    threads: Channellist[thread-specific [channel](
    """ DOCS_RESOURCES_CHANNEL/channel-object) object] """

    users: Userlist[[user](
    """ DOCS_RESOURCES_USER/user-object) object] """

    webhooks: Webhooklist[[webhook](
    """ DOCS_RESOURCES_WEBHOOK/webhook-object) object] """

@dc.dataclass
class AuditLogEntry:
    target_id: strstring | None
    """  """

    changes: AuditLogChangelist[[audit log change]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_RESOURCES_AUDIT_LOG/audit-log-change-object) object] """

    user_id: Snowflakesnowflake | None
    """  """

    id: Snowflake
    """  """

    action_type: AuditLogEvent
    """  """

    options: OptionalAuditEntryInfo | None = dc.field(kw_only=True, default=None)
    """  """

    reason: str | None = dc.field(kw_only=True, default=None)
    """  """

@dc.dataclass
class AuditLogChange:
    new_value: t.Any | None = dc.field(kw_only=True, default=None)
    """   (matches object field's type) """

    old_value: t.Any | None = dc.field(kw_only=True, default=None)
    """   (matches object field's type) """

    key: str
    """ `exceptions` """

@dc.dataclass
class GuildTemplate:
    code: str
    """  """

    name: str
    """  """

    description: strstring | None
    """  """

    usage_count: int
    """  """

    creator_id: Snowflake
    """  """

    creator: User
    """  """

    created_at: str
    """  """

    updated_at: str
    """  """

    source_guild_id: Snowflake
    """  """

    serialized_source_guild: Guild
    """  """

    is_dirty: boolboolean | None
    """  """

@dc.dataclass
class Guild:
    id: Snowflake
    """  """

    name: str
    """  """

    icon: strstring | None
    """ `icon hash` """

    icon_hash: strstring | None = dc.field(kw_only=True, default=None)
    """ `icon hash` """

    splash: strstring | None
    """ `splash hash` """

    discovery_splash: strstring | None
    """ `discovery splash hash` """

    owner: bool | None = dc.field(kw_only=True, default=None)
    """ `the user` """

    owner_id: Snowflake
    """  """

    permissions: str | None = dc.field(kw_only=True, default=None)
    """ `the user` """

    region: strstring | None = dc.field(kw_only=True, default=None)
    """ `voice region` """

    afk_channel_id: Snowflakesnowflake | None
    """  """

    afk_timeout: int
    """  """

    widget_enabled: bool | None = dc.field(kw_only=True, default=None)
    """  """

    widget_channel_id: Snowflakesnowflake | None = dc.field(kw_only=True, default=None)
    """  """

    verification_level: int
    """ `verification level` """

    default_message_notifications: int
    """ `message notifications level` """

    explicit_content_filter: int
    """ `explicit content filter level` """

    roles: Rolelist[[role](
    """ DOCS_TOPICS_PERMISSIONS/role-object) object] """

    emojis: Emojilist[[emoji](
    """ DOCS_RESOURCES_EMOJI/emoji-object) object] """

    features: strGuildFeaturelist[[guild feature](
    """ DOCS_RESOURCES_GUILD/guild-object-guild-features) string] """

    mfa_level: int
    """ `MFA level` """

    application_id: Snowflakesnowflake | None
    """  """

    system_channel_id: Snowflakesnowflake | None
    """  """

    system_channel_flags: int
    """ `system channel flags` """

    rules_channel_id: Snowflakesnowflake | None
    """  """

    max_presences: intinteger | None = dc.field(kw_only=True, default=None)
    """  """

    max_members: int | None = dc.field(kw_only=True, default=None)
    """  """

    vanity_url_code: strstring | None
    """  """

    description: strstring | None
    """  """

    banner: strstring | None
    """ `banner hash` """

    premium_tier: int
    """ `premium tier` """

    premium_subscription_count: int | None = dc.field(kw_only=True, default=None)
    """  """

    preferred_locale: str
    """ `locale` """

    public_updates_channel_id: Snowflakesnowflake | None
    """  """

    max_video_channel_users: int | None = dc.field(kw_only=True, default=None)
    """  """

    max_stage_video_channel_users: int | None = dc.field(kw_only=True, default=None)
    """  """

    approximate_member_count: int | None = dc.field(kw_only=True, default=None)
    """  """

    approximate_presence_count: int | None = dc.field(kw_only=True, default=None)
    """  """

    welcome_screen: WelcomeScreen | None = dc.field(kw_only=True, default=None)
    """ `Invite` """

    nsfw_level: int
    """ `guild NSFW level` """

    stickers: Stickerlist[[sticker]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_RESOURCES_STICKER/sticker-object) object] """

    premium_progress_bar_enabled: bool
    """  """

    safety_alerts_channel_id: Snowflakesnowflake | None
    """  """

@dc.dataclass
class GuildPreview:
    id: Snowflake
    """  """

    name: str
    """  """

    icon: strstring | None
    """ `icon hash` """

    splash: strstring | None
    """ `splash hash` """

    discovery_splash: strstring | None
    """ `discovery splash hash` """

    emojis: Emojilist[[emoji](
    """ DOCS_RESOURCES_EMOJI/emoji-object) object] """

    features: strGuildFeaturelist[[guild feature](
    """ DOCS_RESOURCES_GUILD/guild-object-guild-features) string] """

    approximate_member_count: int
    """  """

    approximate_presence_count: int
    """  """

    description: strstring | None
    """  """

    stickers: Stickerlist[[sticker](
    """ DOCS_RESOURCES_STICKER/sticker-object) object] """

@dc.dataclass
class GuildWidgetSettings:
    enabled: bool
    """  """

    channel_id: Snowflakesnowflake | None
    """  """

@dc.dataclass
class GuildWidget:
    id: Snowflake
    """  """

    name: str
    """  """

    instant_invite: strstring | None
    """  """

    channels: Channellist[partial [channel](
    """ DOCS_RESOURCES_CHANNEL/channel-object) object] """

    members: Userlist[partial [user](
    """ DOCS_RESOURCES_USER/user-object) object] """

    presence_count: int
    """  """

@dc.dataclass
class GuildMember:
    user: User | None = dc.field(kw_only=True, default=None)
    """  """

    nick: strstring | None = dc.field(kw_only=True, default=None)
    """  """

    avatar: strstring | None = dc.field(kw_only=True, default=None)
    """ `guild avatar hash` """

    roles: Snowflakelist[snowflake]
    """ `role` """

    joined_at: str
    """  """

    premium_since: strISO8601 timestamp | None = dc.field(kw_only=True, default=None)
    """ `boosting` """

    deaf: bool
    """  """

    mute: bool
    """  """

    flags: int
    """ `guild member flags` """

    pending: bool | None = dc.field(kw_only=True, default=None)
    """ `Membership Screening` """

    permissions: str | None = dc.field(kw_only=True, default=None)
    """  """

    communication_disabled_until: strISO8601 timestamp | None = dc.field(kw_only=True, default=None)
    """ `timeout` """

@dc.dataclass
class Integration:
    id: Snowflake
    """  """

    name: str
    """  """

    type: str
    """  """

    enabled: bool
    """  """

    syncing: bool | None = dc.field(kw_only=True, default=None)
    """  """

    role_id: Snowflake | None = dc.field(kw_only=True, default=None)
    """  """

    enable_emoticons: bool | None = dc.field(kw_only=True, default=None)
    """  """

    expire_behavior: IntegrationExpireBehavior | None = dc.field(kw_only=True, default=None)
    """  """

    expire_grace_period: int | None = dc.field(kw_only=True, default=None)
    """  """

    user: User | None = dc.field(kw_only=True, default=None)
    """  """

    account: Account
    """  """

    synced_at: str | None = dc.field(kw_only=True, default=None)
    """  """

    subscriber_count: int | None = dc.field(kw_only=True, default=None)
    """  """

    revoked: bool | None = dc.field(kw_only=True, default=None)
    """  """

    application: Application | None = dc.field(kw_only=True, default=None)
    """  """

    scopes: OAuth2Scopeslist[[OAuth2 scopes]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_TOPICS_OAUTH2/shared-resources-oauth2-scopes)] """

@dc.dataclass
class IntegrationAccount:
    id: str
    """  """

    name: str
    """  """

@dc.dataclass
class IntegrationApplication:
    id: Snowflake
    """  """

    name: str
    """  """

    icon: strstring | None
    """ `icon hash` """

    description: str
    """  """

    bot: User | None = dc.field(kw_only=True, default=None)
    """  """

@dc.dataclass
class Ban:
    reason: strstring | None
    """  """

    user: User
    """  """

@dc.dataclass
class WelcomeScreen:
    description: strstring | None
    """  """

    welcome_channels: WelcomeScreenChannellist[[welcome screen channel](
    """ DOCS_RESOURCES_GUILD/welcome-screen-object-welcome-screen-channel-structure) object] """

@dc.dataclass
class WelcomeScreenChannel:
    channel_id: Snowflake
    """  """

    description: str
    """  """

    emoji_id: Snowflakesnowflake | None
    """ `emoji id` """

    emoji_name: strstring | None
    """  """

@dc.dataclass
class GuildOnboarding:
    guild_id: Snowflake
    """  """

    prompts: OnboardingPromptlist[[onboarding prompt](
    """ DOCS_RESOURCES_GUILD/guild-onboarding-object-onboarding-prompt-structure) object] """

    default_channel_ids: Snowflakelist[snowflake]
    """  """

    enabled: bool
    """  """

    mode: OnboardingMode
    """  """

@dc.dataclass
class OnboardingPrompt:
    id: Snowflake
    """  """

    type: PromptType
    """  """

    options: PromptOptionlist[[prompt option](
    """ DOCS_RESOURCES_GUILD/guild-onboarding-object-prompt-option-structure) object] """

    title: str
    """  """

    single_select: bool
    """  """

    required: bool
    """  """

    in_onboarding: bool
    """  """

@dc.dataclass
class PromptOption:
    id: Snowflake
    """  """

    channel_ids: Snowflakelist[snowflake]
    """  """

    role_ids: Snowflakelist[snowflake]
    """  """

    emoji: Emoji
    """  """

    title: str
    """  """

    description: strstring | None
    """  """

@dc.dataclass
class User:
    id: Snowflake
    """  """

    username: str
    """  """

    discriminator: str
    """  """

    global_name: strstring | None
    """  """

    avatar: strstring | None
    """ `avatar hash` """

    bot: bool | None = dc.field(kw_only=True, default=None)
    """  """

    system: bool | None = dc.field(kw_only=True, default=None)
    """  """

    mfa_enabled: bool | None = dc.field(kw_only=True, default=None)
    """  """

    banner: strstring | None = dc.field(kw_only=True, default=None)
    """ `banner hash` """

    accent_color: intinteger | None = dc.field(kw_only=True, default=None)
    """  """

    locale: str | None = dc.field(kw_only=True, default=None)
    """ `language option` """

    verified: bool | None = dc.field(kw_only=True, default=None)
    """  """

    email: strstring | None = dc.field(kw_only=True, default=None)
    """  """

    flags: int | None = dc.field(kw_only=True, default=None)
    """ `flags` """

    premium_type: int | None = dc.field(kw_only=True, default=None)
    """ `type of Nitro subscription` """

    public_flags: int | None = dc.field(kw_only=True, default=None)
    """ `flags` """

    avatar_decoration: strstring | None = dc.field(kw_only=True, default=None)
    """ `avatar decoration hash` """

@dc.dataclass
class Connection:
    id: str
    """  """

    name: str
    """  """

    type: str
    """ `service` """

    revoked: bool | None = dc.field(kw_only=True, default=None)
    """  """

    integrations:  | None = dc.field(kw_only=True, default=None)
    """ `server integrations` """

    verified: bool
    """  """

    friend_sync: bool
    """  """

    show_activity: bool
    """  """

    two_way_link: bool
    """  """

    visibility: int
    """ `visibility` """

@dc.dataclass
class ApplicationRoleConnection:
    platform_name: strstring | None
    """  """

    platform_username: strstring | None
    """  """

    metadata: 
    """ `application role connection metadata` """

@dc.dataclass
class Invite:
    code: str
    """  """

    guild: Guild | None = dc.field(kw_only=True, default=None)
    """  """

    channel: partial [channel](
    """ DOCS_RESOURCES_CHANNEL/channel-object) object | NoneChannel """

    inviter: User | None = dc.field(kw_only=True, default=None)
    """  """

    target_type: int | None = dc.field(kw_only=True, default=None)
    """ `type of target` """

    target_user: User | None = dc.field(kw_only=True, default=None)
    """  """

    target_application: Application | None = dc.field(kw_only=True, default=None)
    """  """

    approximate_presence_count: int | None = dc.field(kw_only=True, default=None)
    """  """

    approximate_member_count: int | None = dc.field(kw_only=True, default=None)
    """  """

    expires_at: strISO8601 timestamp | None = dc.field(kw_only=True, default=None)
    """  """

    stage_instance: InviteStageInstance | None = dc.field(kw_only=True, default=None)
    """ `public Stage instance` """

    guild_scheduled_event: GuildScheduledEvent | None = dc.field(kw_only=True, default=None)
    """  """

@dc.dataclass
class InviteMetadata:
    uses: int
    """  """

    max_uses: int
    """  """

    max_age: int
    """  """

    temporary: bool
    """  """

    created_at: str
    """  """

@dc.dataclass
class InviteStageInstance:
    members: GuildMemberlist[partial [guild member](
    """ DOCS_RESOURCES_GUILD/guild-member-object) object] """

    participant_count: int
    """  """

    speaker_count: int
    """  """

    topic: str
    """  """

@dc.dataclass
class VoiceState:
    guild_id: Snowflake | None = dc.field(kw_only=True, default=None)
    """  """

    channel_id: Snowflakesnowflake | None
    """  """

    user_id: Snowflake
    """  """

    member: GuildMember | None = dc.field(kw_only=True, default=None)
    """  """

    session_id: str
    """  """

    deaf: bool
    """  """

    mute: bool
    """  """

    self_deaf: bool
    """  """

    self_mute: bool
    """  """

    self_stream: bool | None = dc.field(kw_only=True, default=None)
    """  """

    self_video: bool
    """  """

    suppress: bool
    """  """

    request_to_speak_timestamp: strISO8601 timestamp | None
    """  """

@dc.dataclass
class VoiceRegion:
    id: str
    """  """

    name: str
    """  """

    optimal: bool
    """  """

    deprecated: bool
    """  """

    custom: bool
    """  """

@dc.dataclass
class Application:
    id: Snowflake
    """  """

    name: str
    """  """

    icon: strstring | None
    """ `icon hash` """

    description: str
    """  """

    rpc_origins: strlist[string] | None = dc.field(kw_only=True, default=None)
    """  """

    bot_public: bool
    """  """

    bot_require_code_grant: bool
    """  """

    terms_of_service_url: str | None = dc.field(kw_only=True, default=None)
    """  """

    privacy_policy_url: str | None = dc.field(kw_only=True, default=None)
    """  """

    owner: User | None = dc.field(kw_only=True, default=None)
    """  """

    verify_key: str
    """ `GetTicket` """

    team: [team](
    """ DOCS_TOPICS_TEAMS/data-models-team-object) object | NoneTeam """

    guild_id: Snowflake | None = dc.field(kw_only=True, default=None)
    """  """

    guild: Guild | None = dc.field(kw_only=True, default=None)
    """  """

    primary_sku_id: Snowflake | None = dc.field(kw_only=True, default=None)
    """  """

    slug: str | None = dc.field(kw_only=True, default=None)
    """  """

    cover_image: str | None = dc.field(kw_only=True, default=None)
    """ `cover image hash` """

    flags: int | None = dc.field(kw_only=True, default=None)
    """ `flags` """

    approximate_guild_count: int | None = dc.field(kw_only=True, default=None)
    """  """

    tags: strlist[string] | None = dc.field(kw_only=True, default=None)
    """  """

    install_params: InstallParams | None = dc.field(kw_only=True, default=None)
    """  """

    custom_install_url: str | None = dc.field(kw_only=True, default=None)
    """  """

    role_connections_verification_url: str | None = dc.field(kw_only=True, default=None)
    """  """

@dc.dataclass
class InstallParams:
    scopes: strlist[string]
    """ `scopes` """

    permissions: str
    """ `permissions` """

@dc.dataclass
class Webhook:
    id: Snowflake
    """  """

    type: int
    """ `type` """

    guild_id: Snowflakesnowflake | None = dc.field(kw_only=True, default=None)
    """  """

    channel_id: Snowflakesnowflake | None
    """  """

    user: User | None = dc.field(kw_only=True, default=None)
    """  """

    name: strstring | None
    """  """

    avatar: strstring | None
    """ `hash` """

    token: str | None = dc.field(kw_only=True, default=None)
    """  """

    application_id: Snowflakesnowflake | None
    """  """

    source_guild: Guild | None = dc.field(kw_only=True, default=None)
    """  """

    source_channel: Channel | None = dc.field(kw_only=True, default=None)
    """  """

    url: str | None = dc.field(kw_only=True, default=None)
    """ `webhooks` """

@dc.dataclass
class ApplicationRoleConnectionMetadata:
    type: ApplicationRoleConnectionMetadataType
    """  """

    key: str
    """  """

    name: str
    """  """

    name_localizations: AvailableLocales | None = dc.field(kw_only=True, default=None)
    """  """

    description: str
    """  """

    description_localizations: AvailableLocales | None = dc.field(kw_only=True, default=None)
    """  """

@dc.dataclass
class Channel:
    id: Snowflake
    """  """

    type: int
    """ `type of channel` """

    guild_id: Snowflake | None = dc.field(kw_only=True, default=None)
    """  """

    position: int | None = dc.field(kw_only=True, default=None)
    """  """

    permission_overwrites: Overwritelist[[overwrite]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_RESOURCES_CHANNEL/overwrite-object) object] """

    name: strstring | None = dc.field(kw_only=True, default=None)
    """  """

    topic: strstring | None = dc.field(kw_only=True, default=None)
    """  """

    nsfw: bool | None = dc.field(kw_only=True, default=None)
    """  """

    last_message_id: Snowflakesnowflake | None = dc.field(kw_only=True, default=None)
    """  """

    bitrate: int | None = dc.field(kw_only=True, default=None)
    """  """

    user_limit: int | None = dc.field(kw_only=True, default=None)
    """  """

    rate_limit_per_user: int | None = dc.field(kw_only=True, default=None)
    """  """

    recipients: Userlist[[user]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_RESOURCES_USER/user-object) object] """

    icon: strstring | None = dc.field(kw_only=True, default=None)
    """  """

    owner_id: Snowflake | None = dc.field(kw_only=True, default=None)
    """  """

    application_id: Snowflake | None = dc.field(kw_only=True, default=None)
    """  """

    managed: bool | None = dc.field(kw_only=True, default=None)
    """  """

    parent_id: Snowflakesnowflake | None = dc.field(kw_only=True, default=None)
    """  """

    last_pin_timestamp: strISO8601 timestamp | None = dc.field(kw_only=True, default=None)
    """  """

    rtc_region: strstring | None = dc.field(kw_only=True, default=None)
    """ `voice region` """

    video_quality_mode: int | None = dc.field(kw_only=True, default=None)
    """ `video quality mode` """

    message_count: int | None = dc.field(kw_only=True, default=None)
    """  """

    member_count: int | None = dc.field(kw_only=True, default=None)
    """  """

    thread_metadata: ThreadMetadata | None = dc.field(kw_only=True, default=None)
    """  """

    member: ThreadMember | None = dc.field(kw_only=True, default=None)
    """  """

    default_auto_archive_duration: int | None = dc.field(kw_only=True, default=None)
    """  """

    permissions: str | None = dc.field(kw_only=True, default=None)
    """  """

    flags: int | None = dc.field(kw_only=True, default=None)
    """ `channel flags` """

    total_message_sent: int | None = dc.field(kw_only=True, default=None)
    """  """

    available_tags: Taglist[[tag]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_RESOURCES_CHANNEL/forum-tag-object) object] """

    applied_tags: Snowflakelist[snowflake] | None = dc.field(kw_only=True, default=None)
    """  """

    default_reaction_emoji: [default reaction]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_RESOURCES_CHANNEL/default-reaction-object) object | NoneDefaultReaction """

    default_thread_rate_limit_per_user: int | None = dc.field(kw_only=True, default=None)
    """  """

    default_sort_order: intinteger | None = dc.field(kw_only=True, default=None)
    """ `default sort order type` """

    default_forum_layout: int | None = dc.field(kw_only=True, default=None)
    """ `default forum layout view` """

@dc.dataclass
class Message:
    id: Snowflake
    """  """

    channel_id: Snowflake
    """  """

    author: User
    """  """

    content: str
    """  """

    timestamp: str
    """  """

    edited_timestamp: strISO8601 timestamp | None
    """  """

    tts: bool
    """  """

    mention_everyone: bool
    """  """

    mentions: Userlist[[user](
    """ DOCS_RESOURCES_USER/user-object) object] """

    mention_roles: Rolelist[[role](
    """ DOCS_TOPICS_PERMISSIONS/role-object) object id] """

    mention_channels: ChannelMentionlist[[channel mention]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_RESOURCES_CHANNEL/channel-mention-object) object] """

    attachments: Attachmentlist[[attachment](
    """ DOCS_RESOURCES_CHANNEL/attachment-object) object] """

    embeds: Embedlist[[embed](
    """ DOCS_RESOURCES_CHANNEL/embed-object) object] """

    reactions: Reactionlist[[reaction]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_RESOURCES_CHANNEL/reaction-object) object] """

    nonce: strint | None = dc.field(kw_only=True, default=None)
    """  """

    pinned: bool
    """  """

    webhook_id: Snowflake | None = dc.field(kw_only=True, default=None)
    """  """

    type: int
    """ `type of message` """

    activity: MessageActivity | None = dc.field(kw_only=True, default=None)
    """  """

    application: Application | None = dc.field(kw_only=True, default=None)
    """  """

    application_id: Snowflake | None = dc.field(kw_only=True, default=None)
    """ `Interaction` """

    message_reference: MessageReference | None = dc.field(kw_only=True, default=None)
    """  """

    flags: int | None = dc.field(kw_only=True, default=None)
    """ `message flags` """

    referenced_message: [message object]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_RESOURCES_CHANNEL/message-object) | NoneMessageObject """

    interaction: MessageInteractionObject | None = dc.field(kw_only=True, default=None)
    """ `Interaction` """

    thread: Channel | None = dc.field(kw_only=True, default=None)
    """ `thread member` """

    components: MessageComponentslist[[message components]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_INTERACTIONS_MESSAGE_COMPONENTS/component-object)] """

    sticker_items: MessageStickerItemObjectslist[[message sticker item objects]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_RESOURCES_STICKER/sticker-item-object)] """

    stickers: Stickerlist[[sticker]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_RESOURCES_STICKER/sticker-object) object] """

    position: int | None = dc.field(kw_only=True, default=None)
    """  """

    role_subscription_data: RoleSubscriptionData | None = dc.field(kw_only=True, default=None)
    """  """

@dc.dataclass
class MessageActivity:
    type: int
    """ `type of message activity` """

    party_id: str | None = dc.field(kw_only=True, default=None)
    """ `Rich Presence event` """

@dc.dataclass
class MessageReference:
    message_id: Snowflake | None = dc.field(kw_only=True, default=None)
    """  """

    channel_id: Snowflake | None = dc.field(kw_only=True, default=None)
    """  """

    guild_id: Snowflake | None = dc.field(kw_only=True, default=None)
    """  """

    fail_if_not_exists: bool | None = dc.field(kw_only=True, default=None)
    """  """

@dc.dataclass
class FollowedChannel:
    channel_id: Snowflake
    """  """

    webhook_id: Snowflake
    """  """

@dc.dataclass
class Reaction:
    count: int
    """  """

    me: bool
    """  """

    emoji: Emoji
    """  """

@dc.dataclass
class Overwrite:
    id: Snowflake
    """  """

    type: 
    """  """

    allow: str
    """  """

    deny: str
    """  """

@dc.dataclass
class ThreadMetadata:
    archived: bool
    """  """

    auto_archive_duration: int
    """  """

    archive_timestamp: str
    """  """

    locked: bool
    """  """

    invitable: bool | None = dc.field(kw_only=True, default=None)
    """  """

    create_timestamp: strISO8601 timestamp | None = dc.field(kw_only=True, default=None)
    """  """

@dc.dataclass
class ThreadMember:
    id: Snowflake | None = dc.field(kw_only=True, default=None)
    """  """

    user_id: Snowflake | None = dc.field(kw_only=True, default=None)
    """  """

    join_timestamp: str
    """  """

    flags: int
    """  """

    member: GuildMember | None = dc.field(kw_only=True, default=None)
    """  """

@dc.dataclass
class DefaultReaction:
    emoji_id: Snowflakesnowflake | None
    """  """

    emoji_name: strstring | None
    """  """

@dc.dataclass
class ForumTag:
    id: Snowflake
    """  """

    name: str
    """  """

    moderated: bool
    """  """

    emoji_id: Snowflakesnowflake | None
    """  """

    emoji_name: strstring | None
    """  """

@dc.dataclass
class Embed:
    title: str | None = dc.field(kw_only=True, default=None)
    """  """

    type: str | None = dc.field(kw_only=True, default=None)
    """ `type of embed` """

    description: str | None = dc.field(kw_only=True, default=None)
    """  """

    url: str | None = dc.field(kw_only=True, default=None)
    """  """

    timestamp: str | None = dc.field(kw_only=True, default=None)
    """  """

    color: int | None = dc.field(kw_only=True, default=None)
    """  """

    footer: EmbedFooter | None = dc.field(kw_only=True, default=None)
    """  """

    image: EmbedImage | None = dc.field(kw_only=True, default=None)
    """  """

    thumbnail: EmbedThumbnail | None = dc.field(kw_only=True, default=None)
    """  """

    video: EmbedVideo | None = dc.field(kw_only=True, default=None)
    """  """

    provider: EmbedProvider | None = dc.field(kw_only=True, default=None)
    """  """

    author: EmbedAuthor | None = dc.field(kw_only=True, default=None)
    """  """

    fields: EmbedFieldlist[[embed field]( | None = dc.field(kw_only=True, default=None)
    """ DOCS_RESOURCES_CHANNEL/embed-object-embed-field-structure) object] """

@dc.dataclass
class EmbedThumbnail:
    url: str
    """  """

    proxy_url: str | None = dc.field(kw_only=True, default=None)
    """  """

    height: int | None = dc.field(kw_only=True, default=None)
    """  """

    width: int | None = dc.field(kw_only=True, default=None)
    """  """

@dc.dataclass
class EmbedVideo:
    url: str | None = dc.field(kw_only=True, default=None)
    """  """

    proxy_url: str | None = dc.field(kw_only=True, default=None)
    """  """

    height: int | None = dc.field(kw_only=True, default=None)
    """  """

    width: int | None = dc.field(kw_only=True, default=None)
    """  """

@dc.dataclass
class EmbedImage:
    url: str
    """  """

    proxy_url: str | None = dc.field(kw_only=True, default=None)
    """  """

    height: int | None = dc.field(kw_only=True, default=None)
    """  """

    width: int | None = dc.field(kw_only=True, default=None)
    """  """

@dc.dataclass
class EmbedProvider:
    name: str | None = dc.field(kw_only=True, default=None)
    """  """

    url: str | None = dc.field(kw_only=True, default=None)
    """  """

@dc.dataclass
class EmbedAuthor:
    name: str
    """  """

    url: str | None = dc.field(kw_only=True, default=None)
    """  """

    icon_url: str | None = dc.field(kw_only=True, default=None)
    """  """

    proxy_icon_url: str | None = dc.field(kw_only=True, default=None)
    """  """

@dc.dataclass
class EmbedFooter:
    text: str
    """  """

    icon_url: str | None = dc.field(kw_only=True, default=None)
    """  """

    proxy_icon_url: str | None = dc.field(kw_only=True, default=None)
    """  """

@dc.dataclass
class EmbedField:
    name: str
    """  """

    value: str
    """  """

    inline: bool | None = dc.field(kw_only=True, default=None)
    """  """

@dc.dataclass
class Attachment:
    id: Snowflake
    """  """

    filename: str
    """  """

    description: str | None = dc.field(kw_only=True, default=None)
    """  """

    content_type: str | None = dc.field(kw_only=True, default=None)
    """ `media type` """

    size: int
    """  """

    url: str
    """  """

    proxy_url: str
    """  """

    height: intinteger | None = dc.field(kw_only=True, default=None)
    """  """

    width: intinteger | None = dc.field(kw_only=True, default=None)
    """  """

    ephemeral: bool | None = dc.field(kw_only=True, default=None)
    """  """

    duration_secs:  | None = dc.field(kw_only=True, default=None)
    """  """

    waveform: str | None = dc.field(kw_only=True, default=None)
    """  """

    flags: int | None = dc.field(kw_only=True, default=None)
    """ `attachment flags` """

@dc.dataclass
class ChannelMention:
    id: Snowflake
    """  """

    guild_id: Snowflake
    """  """

    type: int
    """ `type of channel` """

    name: str
    """  """

@dc.dataclass
class AllowedMentions:
    parse: list[allowed mention type]
    """ `allowed mention types` """

    roles: Snowflakelist[snowflake]
    """  """

    users: Snowflakelist[snowflake]
    """  """

    replied_user: bool
    """  """

@dc.dataclass
class RoleSubscriptionDataObject:
    role_subscription_listing_id: Snowflake
    """  """

    tier_name: str
    """  """

    total_months_subscribed: int
    """  """

    is_renewal: bool
    """  """

@dc.dataclass
class GuildScheduledEvent:
    id: Snowflake
    """  """

    guild_id: Snowflake
    """  """

    channel_id: Snowflakesnowflake | None
    """ `scheduled entity type` """

    creator_id: Snowflakesnowflake | None = dc.field(kw_only=True, default=None)
    """  """

    name: str
    """  """

    description: strstring | None = dc.field(kw_only=True, default=None)
    """  """

    scheduled_start_time: str
    """  """

    scheduled_end_time: strISO8601 timestamp | None
    """  """

    privacy_level: PrivacyLevel
    """  """

    status: EventStatus
    """  """

    entity_type: ScheduledEntityType
    """  """

    entity_id: Snowflakesnowflake | None
    """  """

    entity_metadata: [entity metadata](
    """ DOCS_RESOURCES_GUILD_SCHEDULED_EVENT/guild-scheduled-event-object-guild-scheduled-event-entity-metadata) | NoneEntityMetadata """

    creator: User | None = dc.field(kw_only=True, default=None)
    """  """

    user_count: int | None = dc.field(kw_only=True, default=None)
    """  """

    image: strstring | None = dc.field(kw_only=True, default=None)
    """ `cover image hash` """

@dc.dataclass
class GuildScheduledEventUser:
    guild_scheduled_event_id: Snowflake
    """  """

    user: User
    """  """

    member: GuildMember | None = dc.field(kw_only=True, default=None)
    """  """

@dc.dataclass
class Response:
    application: Application
    """  """

    scopes: strlist[string]
    """  """

    expires: str
    """  """

    user: User | None = dc.field(kw_only=True, default=None)
    """  """

@dc.dataclass
class Role:
    id: Snowflake
    """  """

    name: str
    """  """

    color: int
    """  """

    hoist: bool
    """  """

    icon: strstring | None = dc.field(kw_only=True, default=None)
    """ `icon hash` """

    unicode_emoji: strstring | None = dc.field(kw_only=True, default=None)
    """  """

    position: int
    """  """

    permissions: str
    """  """

    managed: bool
    """  """

    mentionable: bool
    """  """

    tags: RoleTags | None = dc.field(kw_only=True, default=None)
    """  """

    flags: int
    """ `role flags` """

@dc.dataclass
class RoleTags:
    bot_id: Snowflake | None = dc.field(kw_only=True, default=None)
    """  """

    integration_id: Snowflake | None = dc.field(kw_only=True, default=None)
    """  """

    premium_subscriber:  | None = dc.field(kw_only=True, default=None)
    """  """

    subscription_listing_id: Snowflake | None = dc.field(kw_only=True, default=None)
    """  """

    available_for_purchase:  | None = dc.field(kw_only=True, default=None)
    """  """

    guild_connections:  | None = dc.field(kw_only=True, default=None)
    """  """

