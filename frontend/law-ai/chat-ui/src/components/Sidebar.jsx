import React, { useState } from "react";
import { Plus, Search, Image, FolderOpen, Sparkles } from "lucide-react";
import SidebarItem from "./SidebarItem";
import ChatHistory from "./ChatHistory";
import UserProfile from "./UserProfile";

export default function Sidebar({
  chats,
  activeChat,
  onChatSelect,
  onNewChat,
  onDeleteChat,
}) {
  const [searchQuery, setSearchQuery] = useState("");

  return (
    <div className="w-72 bg-slate-900 text-slate-100 flex flex-col h-screen">
      {/* New Chat */}
      <div className="p-4">
        <button
          onClick={onNewChat}
          className="w-full flex items-center justify-center gap-2 bg-slate-800 hover:bg-slate-700 rounded-xl py-2.5 text-sm font-medium transition"
        >
          <Plus size={18} />
          New chat
        </button>
      </div>

      {/* Search */}
      <div className="px-4 pb-3">
        <div className="relative">
          <Search
            size={16}
            className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400"
          />
          <input
            type="text"
            placeholder="Search"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full pl-9 pr-3 py-2 rounded-lg bg-slate-800 text-sm placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-slate-600"
          />
        </div>
      </div>

      
      {/* Chats */}
      <div className="flex-1 mt-4 overflow-y-auto">
        <ChatHistory
          chats={chats}
          activeChat={activeChat}
          onChatSelect={onChatSelect}
          onDeleteChat={onDeleteChat}
        />
      </div>

      {/* Profile */}
      <div className="p-4 border-t border-slate-800">
        <UserProfile />
      </div>
    </div>
  );
}
