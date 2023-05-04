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

function _G.set_terminal_keymaps()
    local opts = { buffer = 0 }
    vim.keymap.set("t", "<esc>", [[<C-t><C-n>]], opts)
    vim.keymap.set("t", "jk", [[<C-t><C-n>]], opts)
    vim.keymap.set("t", "<C-h>", [[<Cmd>wincmd h<CR>]], opts)
    vim.keymap.set("t", "<C-j>", [[<Cmd>wincmd j<CR>]], opts)
    vim.keymap.set("t", "<C-k>", [[<Cmd>wincmd k<CR>]], opts)
    vim.keymap.set("t", "<C-l>", [[<Cmd>wincmd l<CR>]], opts)
    vim.keymap.set("t", "<C-w>", [[<C-t><C-n><C-w>]], opts)
end

-- if you only want these mappings for toggle term use term://*toggleterm#* instead
vim.cmd("autocmd! TermOpen term://* lua set_terminal_keymaps()")
