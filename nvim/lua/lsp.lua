-- Initialize Packer and add plugins
require('pckr').add({
  'hrsh7th/nvim-cmp',
  'hrsh7th/cmp-nvim-lsp',
  'hrsh7th/cmp-buffer',
  'hrsh7th/cmp-path',
  'hrsh7th/cmp-cmdline',
  'L3MON4D3/LuaSnip',
  'saadparwaiz1/cmp_luasnip',
  'neovim/nvim-lspconfig',
  'rafamadriz/friendly-snippets',
})

-- Configure nvim-cmp
local cmp = require'cmp'
cmp.setup({
  snippet = {
    expand = function(args)
      require("luasnip.loaders.from_vscode").lazy_load()
      require('luasnip').lsp_expand(args.body)
    end,
  },
  mapping = cmp.mapping.preset.insert({
    ['<C-b>'] = cmp.mapping.scroll_docs(-4),
    ['<C-f>'] = cmp.mapping.scroll_docs(4),
    ['<C-Space>'] = cmp.mapping.complete(),
    ['<C-e>'] = cmp.mapping.abort(),
    ['<CR>'] = cmp.mapping.confirm({ select = true }),
  }),
  sources = cmp.config.sources({
    { name = 'nvim_lsp' },
    { name = 'luasnip' },  -- For LuaSnip users
  }, {
    { name = 'buffer' },
  })
})

local lspconfig = require('lspconfig')
local servers = { 'clangd', 'rust_analyzer', 'jdtls', 'pyright', 'bashls', 'gopls', 'docker_compose_language_service', 'docker_language_server'}
for _, lsp in ipairs(servers) do
  vim.lsp.enable(lsp)
end

require'lspconfig'.lua_ls.setup {
    settings = {
        Lua = {
            runtime = {
                version = 'LuaJIT',
            },
            workspace = {
                library = {
                    "/home/rishy/repos/lovr-docs",
                },
                checkThirdParty = false,
            },
        },
    },
}
require("luasnip.loaders.from_vscode").lazy_load()

vim.diagnostic.config({
  virtual_text = { current_line = true }
})

