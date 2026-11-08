# Kite, as the pages were opened

Two pages were opened. Do not add a tool they do not list. Do not treat a search snippet as a third page.

## Product page

`https://zerodha.com/products/mcp/`

The page says login is via Kite, with no password or credential sharing with the AI tool, and that access is read-only and can be revoked. It names Claude Desktop, Cursor, Visual Studio Code, Windsurf, and Claude CLI on Linux. It does not print the server URL. It says the bridge is Kite Connect.

## Server repository

`https://github.com/zerodha/kite-mcp-server`

The README says the hosted endpoint is `https://mcp.kite.trade/mcp`, and that `/sse` is also available. It says the hosted version needs no installation and no API key on the user's side. For Claude Desktop it prints this client config:

```json
{
  "mcpServers": {
    "kite": {
      "command": "npx",
      "args": ["mcp-remote", "https://mcp.kite.trade/mcp"]
    }
  }
}
```

That block is for the user's own client. It is not a file in this pack.

The README says the hosted server excludes destructive trading operations. It also says a self-hosted server, with the user's own API key and secret, can expose the other operations. This pack does not run that server and does not store the key.

Tools the README lists, grouped as it groups them:

- Sign-in: `login`
- Market data: `get_quotes`, `get_ltp`, `get_ohlc`, `get_historical_data`, `search_instruments`
- Account: `get_profile`, `get_margins`, `get_holdings`, `get_positions`, `get_mf_holdings`
- Orders: `place_order`, `modify_order`, `cancel_order`, `get_orders`, `get_trades`, `get_order_history`, `get_order_trades`
- GTT: `get_gtts`, `place_gtt_order`, `modify_gtt_order`, `delete_gtt_order`

`login` may be called only to surface the authorization link the tool returns. Do not pass a password. The read tools may be called when the user asked and the session exposes that tool. The six tools that place, modify, or cancel an order or a GTT are not called. `get_gtts` is a read of triggers that already exist. It is not permission to add one.

`EXCLUDED_TOOLS` is the README's own switch for a self-hosted process. This pack does not set it, because this pack does not start the process.
