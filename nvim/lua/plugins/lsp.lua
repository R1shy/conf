return {

{ "saghen/blink.cmp",
  version = 'v0.*',

  ---@module 'blink.cmp'
  ---@type blink.cmp.Config
  opts = {
    keymap = { preset = 'enter' },

    sources = {
      default = { 'lsp', 'path', 'snippets', 'buffer' },
    },
  },
  opts_extend = { "sources.default" }
},
{
  'neovim/nvim-lspconfig',
  dependencies = { 'saghen/blink.cmp' },
  opts = {
    servers = {
      rust_analyzer = {},
      gopls = {},
      clangd = {},
      lua_ls = {},
      cssls = {},
      html = {},

  }},
	config = function(_, opts)
    local lspconfig = require('lspconfig')
    for server, config in pairs(opts.servers) do
      config.capabilities = require('blink.cmp').get_lsp_capabilities(config.capabilities)
      lspconfig[server].setup(config)
    end
  end



},
{
    "folke/lazydev.nvim",
    ft = "lua", -- only load on lua files
    opts = {
      library = {
        { path = "${3rd}/luv/library", words = { "vim%.uv" } },
      },
    },

    {
    "williamboman/mason.nvim"
    }
  }
}
