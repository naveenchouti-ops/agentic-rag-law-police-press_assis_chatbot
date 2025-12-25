import React, { useRef, useEffect } from "react";
import EmptyState from "./EmptyState";
import Messages from "./Messages";
import ChatInput from "./ChatInput";

export default function ChatArea({
  activeChat,
  messages,
  onSendMessage,
  inputText,
  setInputText,
}) {
  const messagesEndRef = useRef(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  return (
    <div className="flex-1 flex flex-col bg-slate-50">
      {/* Messages */}
      <div className="flex-1 overflow-y-auto px-6 py-4">
        {!activeChat ? (
          <EmptyState
            setInputText={setInputText}
            onSendMessage={onSendMessage}   
          />
        ) : (
          <Messages messages={messages} />
        )}
        <div ref={messagesEndRef} />
      </div>

      {/* Input */}
      <div className="border-t border-slate-200 bg-white">
        <ChatInput
          onSendMessage={onSendMessage}
          message={inputText}
          setMessage={setInputText}
        />
      </div>
    </div>
  );
}
