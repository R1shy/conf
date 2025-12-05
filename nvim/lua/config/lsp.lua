
local cmp = require("cmp")
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
    ['<CR>'] = cmp.mapping.confirm({ select = false }),
  }),
  sources = cmp.config.sources({
    { name = 'nvim_lsp' },
    { name = 'luasnip' }, 
  }, {
    { name = 'buffer' },
  })
})

local servers = { 'clangd', 'rust_analyzer', 'pyright', 'bashls', 'lua_ls', 'jdtls'}
for _, lsp in ipairs(servers) do
  vim.lsp.enable(lsp)
end

require("luasnip.loaders.from_vscode").lazy_load()
vim.lsp.inlay_hint.enable(true)
vim.diagnostic.config({
  virtual_text = { current_line = true }
})



