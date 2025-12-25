export async function handleMessage(message) {
  const res = await fetch("http://127.0.0.1:8000/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      chat_id: "test_chat",
      message: message   // ✅ IDHI MAIN FIX
    }),
  });

  if (!res.ok) {
    throw new Error("Backend error");
  }

  const data = await res.json();
  return data;
}
