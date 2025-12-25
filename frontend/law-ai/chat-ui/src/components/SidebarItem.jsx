import React from "react";

export default function SidebarItem({ icon: Icon, label, active = false }) {
  return (
    <button
      className={`w-full flex items-center gap-3 px-3 py-2 rounded-lg text-sm transition
        ${
          active
            ? "bg-slate-800 text-white"
            : "text-slate-300 hover:bg-slate-800 hover:text-white"
        }`}
    >
      <Icon
        size={18}
        className={`${active ? "text-white" : "text-slate-400"}`}
      />
      <span className="truncate">{label}</span>
    </button>
  );
}
