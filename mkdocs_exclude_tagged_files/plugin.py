import typing
from typing import Optional

import frontmatter
import mkdocs.config
import mkdocs.config.config_options
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page


class ExcludeTaggedFilesPluginConfig(mkdocs.config.base.Config):
    tags_to_exclude = mkdocs.config.config_options.Type(list)
    strip_leading_hashtags = mkdocs.config.config_options.Type(bool, default=True)


class ExcludeTaggedFilesPlugin(BasePlugin[ExcludeTaggedFilesPluginConfig]):
    def is_page_excluded(self, meta: typing.Dict):
        if 'tags' in meta:
            for tag in meta['tags']:
                if self.config.strip_leading_hashtags and str(tag).startswith('#'):
                    tag = str(tag)[1:]

                if tag in self.config.tags_to_exclude:
                    return True

            return False

    def on_files(self, files: Files, *, config: MkDocsConfig) -> Optional[Files]:
        for file in files.documentation_pages():
            with open('./docs/' + file.src_uri, 'r') as raw_file:
                metadata = frontmatter.load(raw_file).metadata

                if self.is_page_excluded(metadata):
                    files.remove(file)

        return files

    def on_post_page(self, output: str, *, page: Page, config: MkDocsConfig) -> Optional[str]:
        if self.is_page_excluded(page.meta):
            return ''

        return output
