# Blog Settings
Summary of https://blowfish.page/docs/.
## Color schema
```
# config/_default/params.toml

colorScheme = "blowfish"
```

## Organising content
- https://blowfish.page/docs/getting-started/#organising-content
- https://gohugo.io/content-management/organization/
```
.
├── assets
│   └── img
│       └── author.jpg
├── config
│   └── _default
├── content
│   ├── _index.md
│   ├── about.md
│   └── posts
│       ├── _index.md
│       ├── first-post.md
│       └── another-post
│           ├── aardvark.jpg
│           └── index.md
└── themes
    └── blowfish
```

## Menus
- https://blowfish.page/docs/getting-started/#menus
```
# config/_default/menus.toml

[[main]]
  name = "Blog"
  pageRef = "posts"
  weight = 10

[[main]]
  name = "Topics"
  pageRef = "topics"
  weight = 20

[[main]]
  pre = "github"
  name = "GitHub"
  url = "https://github.com/nunocoracao/blowfish"
  weight = 30

[[main]]
  identifier = "github2"
  pre = "github"
  url = "https://github.com/nunocoracao/blowfish"
  weight = 40

[[footer]]
  name = "Privacy"
  url = "https://external-link"

```

### Site Configurations
- https://blowfish.page/docs/configuration

### Thumbnails
- `feature*` image file is thumbnail.

```
content
└── awesome_article
    ├── index.md
    └── featured.png
```

## Modify the theme
If I change the file of theme, it applys to all pages.
e.g., Apply common google analytics scripts