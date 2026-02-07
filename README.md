# CheatBox

Terminal cheatsheets in a bento box layout.

## Usage

```bash
uv run cheatbox linux       # show linux cheatsheet
uv run cheatbox             # list available cheatsheets
```

## Adding Cheatsheets

Create a YAML file in `data/`:

```yaml
STYLE:
  name: My Tool
  command_width: 20
  outer_width: 135
  primary_color: green

Category Name:
  - command: cmd
    description: what it does
```

## Inspired by

[github.com/fatinul/cheatbox](https://github.com/fatinul/cheatbox)
