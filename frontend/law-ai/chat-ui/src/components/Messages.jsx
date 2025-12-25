import React from "react";
import MessageBubble from "./MessageBubble";

export default function Messages({ messages }) {
  return (
    <div className="max-w-4xl mx-auto w-full">
      <div className="flex flex-col space-y-4">
        {messages.map((message) => (
          <MessageBubble
            key={message.id}
            message={message}
          />
        ))}
      </div>
    </div>
  );
}
