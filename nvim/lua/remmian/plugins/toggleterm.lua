-- import toggleterm plugin safely
local setup, toggleterm = pcall(require, "toggleterm")
if not setup then
    return
end

-- configure/enable toggleterm
toggleterm.setup({
    size = 9,
    open_mapping = [[<C-t>]],
    shade_filetypes = {},
    shade_terminals = true,
    start_in_insert = true,
    shading_factor = 1,
    direction = "float", -- 'vertical' | 'horizontal' | 'tab' | 'float',
    persist_mode = true, -- if set to true (default) the previous terminal mode will be remembered
    persist_size = true,
    float_opts = {
        width = 70,
        height = 15,
        winblend = 3,
        zindex = 1,
    },
    winbar = {
        enabled = false,
        name_formatter = function(term) --  term: Terminal
            return term.name
        end,
    },
})
