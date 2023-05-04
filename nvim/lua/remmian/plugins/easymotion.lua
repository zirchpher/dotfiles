-- import hop plugin safely
local setup, hop = pcall(require, "hop")
if not setup then
    return
end

vim.keymap.set("", "f", function()
    hop.hint_char2({ direction = { nil }, current_line_only = false })
end, { remap = true })
