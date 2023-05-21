-- set leader key to space
vim.g.mapleader = " "

local keymap = vim.keymap -- for conciseness

---------------------
-- General Keymaps
---------------------

-- use jk to exit insert mode
keymap.set("i", "jk", "<ESC>")

-- update nvim
keymap.set("n", "<F5>", ":source%<CR>")

-- save
keymap.set("n", "<C-s>", ":w<CR>")

-- select all
keymap.set("n", "<C-a>", "gg<S-v>G")

-- move entire line
keymap.set("n", "<M-up>", ":m.-2<CR>==")
keymap.set("n", "<M-down>", ":m.+1<CR>==")
keymap.set("i", "<M-up>", "<Esc>:m .-2<CR>==gi")
keymap.set("i", "<M-down>", "<Esc>:m .+1<CR>==gi")

-- copy and paste the current line to up/down
keymap.set("n", "<M-C-down>", "yyp")
keymap.set("n", "<M-C-up>", "yyp")
keymap.set("n", "<M-C-down>", "yyp")
keymap.set("n", "<M-C-up>", "yyp")

-- Resize window
keymap.set("n", "<C-w><left>", "<C-w><")
keymap.set("n", "<C-w><right>", "<C-w>>")
keymap.set("n", "<C-w><up>", "<C-w>+")
keymap.set("n", "<C-w><down>", "<C-w>-")

-- clear search highlights
keymap.set("n", "<leader>nh", ":nohl<CR>")

-- delete single character without copying into register
keymap.set("n", "x", '"_x')

-- Increment/decrement
keymap.set("n", "+", "<C-a>")
keymap.set("n", "-", "<C-x>")

-- window management
keymap.set("n", "<leader>sv", "<C-w>v") -- split window vertically
keymap.set("n", "<leader>sh", "<C-w>s") -- split window horizontally
keymap.set("n", "<leader>se", "<C-w>=") -- make split windows equal width & height
keymap.set("n", "<leader>sx", ":close<CR>") -- close current split window

----------------------
-- Plugin Keybinds
----------------------

-- vim-maximizer
keymap.set("n", "<leader>sm", ":MaximizerToggle<CR>") -- toggle split window maximization

-- nvim-tree
keymap.set("n", "<C-n>", ":NvimTreeToggle<CR>") -- toggle file explorer

-- telescope
keymap.set("n", "<leader>ff", "<cmd>Telescope find_files<cr>") -- find files within current working directory, respects .gitignore
keymap.set("n", "<leader>fs", "<cmd>Telescope live_grep<cr>") -- find string in current working directory as you type
keymap.set("n", "<leader>fc", "<cmd>Telescope grep_string<cr>") -- find string under cursor in current working directory
keymap.set("n", "<leader>fb", "<cmd>Telescope buffers<cr>") -- list open buffers in current neovim instance
keymap.set("n", "<leader>fh", "<cmd>Telescope help_tags<cr>") -- list available help tags

-- telescope git commands (not on youtube nvim video)
keymap.set("n", "<leader>gc", "<cmd>Telescope git_commits<cr>") -- list all git commits (use <cr> to checkout) ["gc" for git commits]
keymap.set("n", "<leader>gfc", "<cmd>Telescope git_bcommits<cr>") -- list git commits for current file/buffer (use <cr> to checkout) ["gfc" for git file commits]
keymap.set("n", "<leader>gb", "<cmd>Telescope git_branches<cr>") -- list git branches (use <cr> to checkout) ["gb" for git branch]
keymap.set("n", "<leader>gs", "<cmd>Telescope git_status<cr>") -- list current changes per file with diff preview ["gs" for git status]

-- MarkdownPreview
keymap.set("n", "<S-tab>", ":MarkdownPreviewToggle<CR>")

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

-- nvim-ufo folding
keymap.set("n", "zO", require("ufo").openAllFolds)
keymap.set("n", "zC", require("ufo").closeAllFolds)

-- restart lsp server (not on youtube nvim video)
keymap.set("n", "<leader>rs", ":LspRestart<CR>") -- mapping to restart lsp if necessary
