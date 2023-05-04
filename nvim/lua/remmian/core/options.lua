local opt = vim.opt -- for conciseness

-- encoding
vim.scriptencoding = "utf-8"
opt.encoding = "utf-8"
opt.fileencoding = "utf-8"

-- line number
opt.relativenumber = true
opt.number = true

-- tabs & indentation
opt.tabstop = 4 -- 4 spaces for tabs (prettier default)
opt.shiftwidth = 4 -- 4 spaces for indent width
opt.expandtab = true -- expand tab to spaces
opt.autoindent = true -- copy indent from current line when starting new one
opt.smartindent = true
opt.breakindent = true

-- line wrapping
opt.wrap = false -- disable line wrapping

-- search settings
opt.ignorecase = true -- ignore case when searching
opt.smartcase = true -- if you include mixed case in your search, assumes you want case-sensitive
opt.hlsearch = true

-- cursor
opt.scrolloff = 10
opt.cursorline = true -- highlight the current cursor line

-- backup
opt.backup = false
opt.backupskip = { "/tmp/*", "/private/tmp/*" }
opt.inccommand = "split"

---------- appearance

-- turn on termguicolors for nightfly colorscheme to work
-- (have to use iterm2 or any other true color terminal)
opt.termguicolors = true
opt.background = "dark" -- colorschemes that can be light or dark will be made dark
opt.signcolumn = "yes" -- show sign column so that text doesn't shift

-- backspace
opt.backspace = { "start", "eol", "indent" }

-- clipboard
opt.clipboard:append("unnamedplus") -- use system clipboard as default register

-- Add asterisks in block comments
opt.formatoptions:append({ "r" })

-- title
opt.title = true

-- split windows
opt.splitright = true -- split vertical window to the right
opt.splitbelow = true -- split horizontal window to the bottom

opt.iskeyword:append("-") -- consider string-string as whole word

-- Undercurl
vim.cmd([[let &t_Cs = "\e[4:3m"]])
vim.cmd([[let &t_Ce = "\e[4:0m"]])

-- Turn off paste mode when leaving insert
vim.api.nvim_create_autocmd("InsertLeave", {
    pattern = "*",
    command = "set nopaste",
})

opt.path:append({ "**" }) -- Finding files - Search down into subfolders
opt.wildignore:append({ "*/node_modules/*" })

-- shell
opt.shell = "zsh"

-- folding
-- opt.foldmethod = "expr"
-- opt.foldexpr = "nvim_treesitter#foldexpr()"

-- local vim = vim
-- local api = vim.api
-- local M = {}
-- -- function to create a list of commands and convert them to autocommands
-- -------- This function is taken from https://github.com/norcalli/nvim_utils
-- function M.nvim_create_augroups(definitions)
--     for group_name, definition in pairs(definitions) do
--         api.nvim_command("augroup " .. group_name)
--         api.nvim_command("autocmd!")
--         for _, def in ipairs(definition) do
--             local command = table.concat(vim.tbl_flatten({ "autocmd", def }), " ")
--             api.nvim_command(command)
--         end
--         api.nvim_command("augroup END")
--     end
-- end
--
-- local autoCommands = {
--     -- other autocommands
--     open_folds = {
--         { "BufReadPost,FileReadPost", "*", "normal zR" },
--     },
-- }
--
-- M.nvim_create_augroups(autoCommands)
