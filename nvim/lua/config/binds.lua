local opts = {}
local map = vim.keymap.set

map("i", "<C-s>", "<Cmd>w<CR>", opts)
map("n", "<C-s>", "<Cmd>w<CR>", opts)
map('i', '<C-Left>', '<Cmd>BufferPrevious<CR>', opts)
map('i', '<C-Right>', '<Cmd>BufferNext<CR>', opts)
map('n', '<C-Left>', '<Cmd>BufferPrevious<CR>', opts)
map('n', '<C-Right>', '<Cmd>BufferNext<CR>', opts)
map('i', '<C-BS>', '<Cmd>BufferClose<CR>', opts)
map('n', '<C-BS>', '<Cmd>BufferClose<CR>', opts)
map('n', '<C-n>', '<Cmd>NvimTreeToggle<CR>', opts)
map('i', '<C-n>', '<Cmd>NvimTreeToggle<CR>', opts)
