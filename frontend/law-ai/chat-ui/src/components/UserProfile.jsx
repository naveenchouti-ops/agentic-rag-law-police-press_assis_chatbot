import React from "react";
import { LogOut } from "lucide-react";

export default function UserProfile() {
  return (
    <div className="space-y-3">
      {/* User info */}
      <div className="flex items-center gap-3 px-2 py-2 rounded-lg hover:bg-slate-1000 transition">
        <div className="w-9 h-9 bg-gradient-to-br from-blue-600 to-purple-800 rounded-full flex items-center justify-center text-white font-semibold text-sm flex-shrink-0">
          A
        </div>

        <div className="flex-1 min-w-0">
          <p className="text-sm font-medium text-slate-100 truncate">
            ""
          </p>
          <p className="text-xs text-slate-400">
            ""
          </p>
        </div>
      </div>

      {/* Sign out */}
      <button className="w-full flex items-center justify-center gap-2 px-3 py-2 rounded-lg text-slate-300 text-sm hover:bg-slate-800 hover:text-white transition">
        <LogOut size={16} />
        Sign out
      </button>
    </div>
  );
}
