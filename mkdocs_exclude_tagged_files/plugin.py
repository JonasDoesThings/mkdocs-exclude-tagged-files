from typing import List, Optional

import mkdocs.config
import mkdocs.config.config_options
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page


class ExcludeTaggedFilesPluginConfig(mkdocs.config.base.Config):
    tags_to_exclude = mkdocs.config.config_options.Type(list)
    strip_leading_hashtags = mkdocs.config.config_options.Type(bool, default=True)


class ExcludeTaggedFilesPlugin(BasePlugin[ExcludeTaggedFilesPluginConfig]):
    def on_post_page(self, output: str, *, page: Page, config: MkDocsConfig) -> Optional[str]:
        if "tags" in page.meta:
            for tag in page.meta["tags"]:
                if self.config.strip_leading_hashtags and str(tag).startswith("#"):
                    tag = str(tag)[1:]

                if tag in self.config.tags_to_exclude:
                    return ""
