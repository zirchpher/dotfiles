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
keymap.set("n", "<M-C-down>", "yyp")
keymap.set("n", "<M-C-up>", "yyp")

-- delete single character without copying into register
keymap.set("n", "x", '"_x')

-- Increment/decrement
keymap.set("n", "+", "<C-a>")
keymap.set("n", "-", "<C-x>")

----------------------
-- Plugin Keybinds
----------------------

-- barbar.nvim
local map = vim.api.nvim_set_keymap
local opts = { noremap = true, silent = true }
-- Move to previous/next
map("n", "<M-.>", "<Cmd>BufferPrevious<CR>", opts)
map("n", "<M-->", "<Cmd>BufferNext<CR>", opts)
map("n", "<M-s-f>", "<Cmd>BufferOrderByDirectory<CR>", opts) -- Re-order tabs
-- Goto buffer in position...
map("n", "<M-1>", "<Cmd>BufferGoto 1<CR>", opts)
map("n", "<M-2>", "<Cmd>BufferGoto 2<CR>", opts)
map("n", "<M-3>", "<Cmd>BufferGoto 3<CR>", opts)
map("n", "<M-4>", "<Cmd>BufferGoto 4<CR>", opts)
map("n", "<M-5>", "<Cmd>BufferGoto 5<CR>", opts)
map("n", "<M-6>", "<Cmd>BufferGoto 6<CR>", opts)
map("n", "<M-7>", "<Cmd>BufferGoto 7<CR>", opts)
map("n", "<M-8>", "<Cmd>BufferGoto 8<CR>", opts)
map("n", "<M-9>", "<Cmd>BufferGoto 9<CR>", opts)
map("n", "<M-0>", "<Cmd>BufferGoto 0<CR>", opts)
map("n", "<M-e>", "<Cmd>BufferPin<CR>", opts) -- Pin/unpin buffer
map("n", "<M-w>", "<Cmd>BufferClose<CR>", opts) -- Close buffer
map("n", "<M-q>", "<Cmd>BufferCloseAllButCurrent<CR>", opts) -- close all buffer

-- MarkdownPreview
keymap.set("n", "<leader>md", ":MarkdownPreviewToggle<CR>")
