### **API Documentation for Dashboard Data Retrieval**

---

### **API Endpoint**

**Base URL**: `http://18.212.37.106/api/dashboard`

### **Request Type**: `GET`

---

### **Purpose**

This API allows users to retrieve the dashboard data associated with a specific **Bot ID**. The data includes metrics like invested amount, net PnL, trading fees, wallet balance, and other trading statistics (rows 1, 2, 3, and 4).

---

### **Request Parameters**

| Parameter | Type   | Description                                      | Required |
|-----------|--------|--------------------------------------------------|----------|
| `bot_id`  | string | The ID of the bot whose dashboard data you want to retrieve. Example: `bot_12345` | Yes      |

---

### **Request Example**

To request the dashboard data for a bot with ID `bot_12345`, you can use the following URL:

```
GET http://18.212.37.106/api/dashboard?bot_id=bot_12345
```

### **Response**

The API will return a JSON object containing the dashboard data for the specified **Bot ID**. The data is structured into four rows, each containing specific metrics as follows:

- **Row 1**:
  - `invested_amount`: Total invested amount.
  - `net_pnl`: Net Profit and Loss.
  - `trading_fees`: Total trading fees.
  - `wallet_balance`: Object containing `spot_balance` and `futures_balance`.

- **Row 2**:
  - `trading_days`: Total number of trading days.
  - `portfolio_growth`: Portfolio growth percentage.
  - `trade_breakdown`: Object containing `total_trades`, `winning_trades`, and `losing_trades`.

- **Row 3**:
  - `win_rate`: Win rate percentage.
  - `risk_reward`: Risk-reward ratio.
  - `max_loss`: Maximum loss value.

- **Row 4**:
  - `trade_outcomes`: Object containing `total_trades`, `winning_trades`, and `losing_trades`.
  - `trade_types`: Object containing `long_trades` and `short_trades`.

---

### **Response Example**

```json
{
  "bot_12345": {
    "row1": {
      "invested_amount": 500,
      "net_pnl": 133.65,
      "trading_fees": 25.61,
      "wallet_balance": {
        "spot_balance": 533,
        "futures_balance": 90
      }
    },
    "row2": {
      "trading_days": 49,
      "portfolio_growth": "26.53%",
      "trade_breakdown": {
        "total_trades": 100,
        "winning_trades": 40,
        "losing_trades": 60
      }
    },
    "row3": {
      "win_rate": "41.92%",
      "risk_reward": 0.97,
      "max_loss": 75
    },
    "row4": {
      "trade_outcomes": {
        "total_trades": 100,
        "winning_trades": 40,
        "losing_trades": 60
      },
      "trade_types": {
        "long_trades": 100,
        "short_trades": 200
      }
    }
  }
}
```

---

### **Error Handling**

If the requested **Bot ID** is not found or is missing from the request, the API will return a `404 Not Found` error.

#### **Error Response Example**:

```json
{
  "error": "Bot ID not found or invalid"
}
```

---

### **How to Test the API**

1. **Using Postman**:
   - Open **Postman**.
   - Create a **GET** request.
   - Set the URL to: `http://18.212.37.106/api/dashboard?bot_id=bot_12345`.
   - Click **Send** to retrieve the dashboard data.

2. **Using cURL**:

   ```bash
   curl "http://18.212.37.106/api/dashboard?bot_id=bot_12345"
   ```

3. **Using Python (requests library)**:

   ```python
   import requests

   url = "http://18.212.37.106/api/dashboard?bot_id=bot_12345"
   response = requests.get(url)
   
   if response.status_code == 200:
       print(response.json())
   else:
       print(f"Error: {response.status_code}")
   ```

---

### **Important Notes**

- Replace `bot_12345` with the actual **Bot ID** to retrieve specific data for other bots.
- The data returned will be specific to the Bot ID provided.
