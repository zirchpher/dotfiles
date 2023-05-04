-- import indent_blankline plugin safely
local setup, indent_blankline = pcall(require, "indent_blankline")
if not setup then
    return
end

vim.opt.list = true
vim.opt.listchars:append("space:⋅")

-- configure/enable indent_blankline
indent_blankline.setup({
    space_char_blankline = " ",
    show_current_context = true,
    show_current_context_start = true,
})
