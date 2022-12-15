# MKDocs Exclude Tagged Files
A simple plugin for excluding files from being included in the mkdocs output based on tags in their frontmatter.

## Configuration
Basic Configuration:
```yaml
plugins:
  - mkdocs_exclude_tagged_files:
      tags_to_exclude: ["confidential", "excluded"]
```
This configuration will exclude all files that have one of the tags "confidential" or "excluded" in their frontmatter.  
For example this file will be excluded:
```markdown
---
tags: ["confidential", "someothertag"]
---
# Content
```

By default, the plugin strips leading `#`-symbols from tags, so the tag `#excluded` will be treated the same as `excluded`.   
If you want to disable this behavior set the config value `strip_leading_hashtags` to `false`.
