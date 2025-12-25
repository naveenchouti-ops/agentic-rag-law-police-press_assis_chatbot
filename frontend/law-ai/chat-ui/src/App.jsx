import React, { useState } from "react";
import Sidebar from "./components/Sidebar";
import ChatArea from "./components/ChatArea";
import Disclaimer from "./components/Disclaimer";
import { handleMessage } from "./utils/handleMessage";

export default function App() {
  // 🔐 Disclaimer
  const [accepted, setAccepted] = useState(false);

  // 💬 Chat state
  const [chats, setChats] = useState([]);
  const [activeChat, setActiveChat] = useState(null);
  const [inputText, setInputText] = useState("");
  const [isTyping, setIsTyping] = useState(false);

  // 🔍 Active chat messages (DERIVED STATE)
  const activeChatData = chats.find((chat) => chat.id === activeChat);
  const messages = activeChatData?.messages || [];

  // ➕ Create new chat
  const handleNewChat = () => {
    const newChat = {
      id: Date.now(),
      title: "New conversation",
      date: "Today",
      messages: [],
    };

    setChats((prev) => [newChat, ...prev]);
    setActiveChat(newChat.id);
    setInputText("");
    setIsTyping(false);
  };

  // 💬 SEND MESSAGE → BACKEND
  const handleSendMessage = async (content) => {
    if (!content.trim()) return;

    let chatId = activeChat;

    // 🧠 Auto-create chat if none
    if (!chatId) {
      chatId = Date.now();

      const newChat = {
        id: chatId,
        title: content.slice(0, 30) || "New conversation",
        date: "Today",
        messages: [],
      };

      setChats((prev) => [newChat, ...prev]);
      setActiveChat(chatId);
    }

    // 👤 Add USER message
    setChats((prev) =>
      prev.map((chat) =>
        chat.id === chatId
          ? {
              ...chat,
              messages: [
                ...chat.messages,
                {
                  id: Date.now(),
                  role: "user",
                  content,
                },
              ],
            }
          : chat
      )
    );

    setInputText("");
    setIsTyping(true);

    try {
      // 🤖 BACKEND CALL
      const reply = await handleMessage(content);

      setChats((prev) =>
        prev.map((chat) =>
          chat.id === chatId
            ? {
                ...chat,
                messages: [
                  ...chat.messages,
                  {
                    id: Date.now(),
                    role: "assistant",
                    content: reply,
                  },
                ],
              }
            : chat
        )
      );
    } catch (error) {
      setChats((prev) =>
        prev.map((chat) =>
          chat.id === chatId
            ? {
                ...chat,
                messages: [
                  ...chat.messages,
                  {
                    id: Date.now(),
                    role: "assistant",
                    content: "❌ Backend connect avvaledhu",
                  },
                ],
              }
            : chat
        )
      );
    }

    setIsTyping(false);
  };

  // 🗑️ Delete chat
  const handleDeleteChat = (chatId) => {
    setChats((prevChats) => {
      const updated = prevChats.filter((chat) => chat.id !== chatId);

      if (activeChat === chatId) {
        setActiveChat(null);
        setInputText("");
        setIsTyping(false);
      }

      return updated;
    });
  };

  // 🧾 UI
  return (
    <>
      {!accepted ? (
        <Disclaimer onAccept={() => setAccepted(true)} />
      ) : (
        <div className="flex h-screen bg-slate-50">
          <Sidebar
            chats={chats}
            activeChat={activeChat}
            onChatSelect={setActiveChat}
            onNewChat={handleNewChat}
            onDeleteChat={handleDeleteChat}
          />

          <ChatArea
            activeChat={activeChat}
            messages={messages}
            onSendMessage={handleSendMessage}
            inputText={inputText}
            setInputText={setInputText}
            isTyping={isTyping}
          />
        </div>
      )}
    </>
  );
}
