
local cmp = require("cmp")
cmp.setup({
  snippet = {
    expand = function(args)
      require("luasnip.loaders.from_vscode").lazy_load()
      require('luasnip').lsp_expand(args.body)
    end,
  },
  window = {
    completion = cmp.config.window.bordered(),
    documentation = cmp.config.window.bordered(),
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

local servers = { 'clangd', 'rust_analyzer', 'pyright', 'bashls', 'lua_ls', 'jdtls', 'ts_ls', 'cssls', 'svls'}

for _, lsp in ipairs(servers) do
  vim.lsp.enable(lsp)
end

require("luasnip.loaders.from_vscode").lazy_load()
vim.lsp.inlay_hint.enable(true)
vim.diagnostic.config({
  virtual_text = { current_line = true }
})

-- Hover documentation keybinding
vim.keymap.set('n', 'K', vim.lsp.buf.hover, { desc = 'Show hover documentation' })

-- Signature help keybinding (shows parameter info while typing)
vim.keymap.set('i', '<C-k>', vim.lsp.buf.signature_help, { desc = 'Show signature help' })

-- Configure hover window
vim.lsp.handlers["textDocument/hover"] = vim.lsp.with(
  vim.lsp.handlers.hover, {
    border = "rounded",
    max_width = 80,
  }
)

-- Configure signature help window
vim.lsp.handlers["textDocument/signatureHelp"] = vim.lsp.with(
  vim.lsp.handlers.signature_help, {
    border = "rounded",
    max_width = 80,
  }
)

-- Auto-show hover on cursor hold (optional - shows docs after pausing cursor)
vim.api.nvim_create_autocmd("CursorHold", {
  callback = function()
    local opts = {
      focusable = false,
      close_events = { "BufLeave", "CursorMoved", "InsertEnter", "FocusLost" },
      border = 'rounded',
      source = 'always',
    }
    vim.diagnostic.open_float(nil, opts)
  end
})

-- Set updatetime for CursorHold event (in milliseconds)
vim.opt.updatetime = 500

require("typescript-tools").setup {
  on_attach = function() end,
  handlers = {},
  settings = {
    separate_diagnostic_server = true,
    publish_diagnostic_on = "change",
    expose_as_code_action = "all",
    tsserver_path = nil,
    tsserver_plugins = {},
    tsserver_max_memory = "auto",
    tsserver_format_options = {},
    tsserver_file_preferences = {},
    tsserver_locale = "en",
    complete_function_calls = true,
    include_completions_with_insert_text = true,
    code_lens = "all",
    disable_member_code_lens = false,
    jsx_close_tag = {
        enable = true,
        filetypes = { "javascriptreact", "typescriptreact" },
    }
  },
}
