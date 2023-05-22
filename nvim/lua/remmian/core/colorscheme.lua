-- set colorscheme to nightfly with protected call
-- in case it isn't installed
-- Colorscheme available
-- nightfly
-- onedark onelight onedark_vivid onedark_dark
-- catppuccin catppuccin-latte, catppuccin-frappe, catppuccin-macchiato, catppuccin-mocha
local status, _ = pcall(vim.cmd, "colorscheme nightfly")
if not status then
    print("Colorscheme not found!") -- print error if colorscheme not installed
    return
end
