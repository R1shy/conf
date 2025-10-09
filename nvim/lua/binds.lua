mode = {"i", "n"}
local opts = {}
vim.keymap.set(mode, "<C-s>", "<Cmd>w<CR>")
vim.keymap.set(mode, '<A-BS>', '<Cmd>BufferClose<CR>', opts)
vim.keymap.set(mode, '<A-Left>', '<Cmd>BufferPrevious<CR>', opts)
vim.keymap.set(mode, '<A-Right>', '<Cmd>BufferNext<CR>', opts)
vim.keymap.set(mode, '<A-n>', '<Cmd>Neotree<CR>', opts)

vim.cmd [[ 


cnoremap <Down> <Nop>
cnoremap <Left> <Nop>
cnoremap <Right> <Nop>
cnoremap <Up> <Nop>
inoremap <Down> <Nop>
inoremap <Left> <Nop>
inoremap <Right> <Nop>
inoremap <Up> <Nop>
nnoremap <Down> <Nop>
nnoremap <Left> <Nop>
nnoremap <Right> <Nop>
nnoremap <Up> <Nop>
vnoremap <Down> <Nop>
vnoremap <Left> <Nop>
vnoremap <Right> <Nop>
vnoremap <Up> <Nop>
]]

vim.opt.mouse = ""
