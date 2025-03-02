vim.cmd [[set number]]
vim.diagnostic.config({
  virtual_text = true, -- Ensures virtual text is always shown
})

local function stop_high_id_clients()
  for _, client in pairs(vim.lsp.get_clients()) do
    if client.id > 1 then
      client.stop()
      print("Stopped LSP client: " .. client.name .. " (ID: " .. client.id .. ")")
    end
  end
end

vim.api.nvim_create_autocmd("LspAttach", {
  callback = function()
    stop_high_id_clients()
  end,
})

vim.cmd([[ augroup ChangeHighlight autocmd! autocmd BufEnter * highlight BufferTabpageFill guibg=#282828 augroup END ]])
