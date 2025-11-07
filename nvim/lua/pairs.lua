require('pckr').add(
{'m4xshen/autoclose.nvim',
{'nvim-treesitter/nvim-treesitter', branch='main'},
'windwp/nvim-ts-autotag'
}
)
require'nvim-treesitter'.setup {
  install_dir = vim.fn.stdpath('data') .. '/site'
}
require('autoclose').setup()
require'nvim-treesitter'.install { 'tsx', 'typescript' }
require('nvim-ts-autotag').setup({
  opts = {
    -- Defaults
    enable_close = true, -- Auto close tags
    enable_rename = true, -- Auto rename pairs of tags
    enable_close_on_slash = false -- Auto close on trailing </
  },
  })
