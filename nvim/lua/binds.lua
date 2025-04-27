local mode = {"i", "n"}
local opts = {}
vim.keymap.set(mode, "<C-s>", "<Cmd>w<CR>")
vim.keymap.set(mode, '<C-BS>', '<Cmd>BufferClose<CR>', opts)
vim.keymap.set(mode, '<C-Left>', '<Cmd>BufferPrevious<CR>', opts)
vim.keymap.set(mode, '<C-Right>', '<Cmd>BufferNext<CR>', opts)
vim.keymap.set(mode, '<C-n>', '<Cmd>Neotree<CR>', opts)

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

vim.keymap.set("", "<up>", "<nop>", { noremap = true })
vim.keymap.set("", "<down>", "<nop>", { noremap = true })
vim.keymap.set("i", "<up>", "<nop>", { noremap = true })
vim.keymap.set("i", "<down>", "<nop>", { noremap = true })

vim.opt.mouse = ""
