local mode = {"i", "n"}
local opts = {}
vim.keymap.set(mode, "<C-s>", "<Cmd>w<CR>")
vim.keymap.set(mode, '<C-BS>', '<Cmd>BufferClose<CR>', opts)
vim.keymap.set(mode, '<C-Left>', '<Cmd>BufferPrevious<CR>', opts)
vim.keymap.set(mode, '<C-Right>', '<Cmd>BufferNext<CR>', opts)
vim.keymap.set(mode, '<C-n>', '<Cmd>Neotree<CR>', opts)
