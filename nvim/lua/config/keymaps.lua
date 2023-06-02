-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here

-- set leader key to space
vim.g.mapleader = " "

local keymap = vim.keymap -- for conciseness

---------------------
-- General Keymaps
---------------------

-- use jk to exit insert mode
keymap.set("i", "jk", "<ESC>")

-- use ; to enter word change mode
keymap.set("n", ";", ":%s/")

-- update nvim
keymap.set("n", "<F5>", ":source%<CR>")

-- select all
keymap.set("n", "<C-a>", "gg<S-v>G")

-- copy and paste the current line to up/down
keymap.set("n", "<M-C-k>", "yyp")
keymap.set("n", "<M-C-j>", "yyp")

-- delete single character without copying into register
keymap.set("n", "x", '"_x')

-- Increment/decrement
keymap.set("n", "+", "<C-a>")
keymap.set("n", "-", "<C-x>")

----------------------
-- Plugin Keybinds
----------------------

-- MarkdownPreview
keymap.set("n", "<leader>md", ":MarkdownPreviewToggle<CR>")

-- easyemotion
vim.keymap.set("", "f", function()
  require("hop").hint_char1({
    direction = { nil },
    current_line_only = false,
  })
end, { remap = true })

-- ChatGPT
-- vim.keymap.set('n', '<Leader>tk', '<cmd>:ChatGPT<cr>')
-- vim.keymap.set('n', '<Leader>tj', '<cmd>:ChatGPTActAs<cr>')
-- vim.keymap.set('n', '<Leader>tt', '<cmd>:ChatGPTEditWithInstructions<cr>
