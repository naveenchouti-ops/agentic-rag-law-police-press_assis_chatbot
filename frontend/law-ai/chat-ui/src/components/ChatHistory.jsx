import React from "react";
import { Trash2 } from "lucide-react";

export default function ChatHistory({
  chats,
  activeChat,
  onChatSelect,
  onDeleteChat, // ⭐ ADD THIS
}) {
  return (
    <div className="h-full overflow-y-auto px-2">
      <p className="px-3 py-2 text-xs font-semibold text-slate-400 uppercase">
        Your chats
      </p>

      <div className="space-y-1">
        {chats.map((chat) => (
          <div
            key={chat.id}
            onClick={() => onChatSelect(chat.id)}
            className={`group flex items-center justify-between gap-2 px-3 py-2 rounded-lg cursor-pointer transition
              ${
                activeChat === chat.id
                  ? "bg-slate-800 text-white"
                  : "text-slate-300 hover:bg-slate-800 hover:text-white"
              }`}
          >
            {/* Text */}
            <div className="flex-1 min-w-0">
              <p className="text-sm truncate">{chat.title}</p>
              <p
                className={`text-xs ${
                  activeChat === chat.id
                    ? "text-slate-400"
                    : "text-slate-500"
                }`}
              >
                {chat.date}
              </p>
            </div>

            {/* Delete */}
            <button
              onClick={(e) => {
                e.stopPropagation();
                onDeleteChat(chat.id); // ⭐ REAL DELETE
              }}
              className="opacity-0 group-hover:opacity-100 p-1 rounded hover:bg-slate-700 transition"
            >
              <Trash2 size={14} className="text-slate-400" />
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}
