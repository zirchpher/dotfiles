-- Lazy setup
require("remmian.plugins.init")

-- Core config
require("remmian.core.options")
require("remmian.core.keymaps")
require("remmian.core.colorscheme")

-- Plugins config
require("remmian.plugins.config.comment")
require("remmian.plugins.config.nvim-tree")
require("remmian.plugins.config.lualine")
require("remmian.plugins.config.telescope")
require("remmian.plugins.config.autopairs")
require("remmian.plugins.config.gitsigns")
require("remmian.plugins.config.treesitter")
require("remmian.plugins.config.colorizer")
require("remmian.plugins.config.indent_blankline")
require("remmian.plugins.config.easymotion")
require("remmian.plugins.config.toggleterm")
require("remmian.plugins.config.markdown")
require("remmian.plugins.config.nvim-ufo")
require("remmian.plugins.config.nvim-cmp")

-- LSP Config
require("remmian.plugins.config.lsp.mason")
require("remmian.plugins.config.lsp.lspkind")
require("remmian.plugins.config.lsp.lspsaga")
require("remmian.plugins.config.lsp.lspconfig")
require("remmian.plugins.config.lsp.null-ls")
