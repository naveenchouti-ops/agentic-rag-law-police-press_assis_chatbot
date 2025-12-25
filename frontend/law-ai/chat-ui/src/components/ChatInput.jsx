import React, { useRef } from "react";
import { Plus, Send } from "lucide-react";

export default function ChatInput({
  onSendMessage,
  message,
  setMessage,
}) {
  const textareaRef = useRef(null);
  const fileInputRef = useRef(null);

  const handleSend = () => {
    if (!message.trim()) return;
    onSendMessage(message);
    setMessage("");
    if (textareaRef.current) {
      textareaRef.current.style.height = "auto";
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  const handleChange = (e) => {
    setMessage(e.target.value);
    if (textareaRef.current) {
      textareaRef.current.style.height = "auto";
      textareaRef.current.style.height =
        Math.min(textareaRef.current.scrollHeight, 140) + "px";
    }
  };

  // 📎 Handle file select
  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (!file) return;

    // For now just show file name in input
    setMessage((prev) => prev + `\n📎 ${file.name}`);
  };

  return (
    <div className="bg-white border-t border-slate-200 py-4">
      <div className="max-w-4xl mx-auto px-4">
        <div className="flex items-end gap-3 bg-slate-100 rounded-2xl px-4 py-3 shadow-sm">

          {/* 📎 Attach */}
          <button
            onClick={() => fileInputRef.current.click()}
            className="text-slate-500 hover:text-slate-700 transition p-1"
            title="Add photos & files"
          >
            <Plus size={18} />
          </button>

          {/* Hidden file input */}
          <input
            ref={fileInputRef}
            type="file"
            className="hidden"
            onChange={handleFileChange}
          />

          {/* Input */}
          <textarea
            ref={textareaRef}
            value={message}
            onChange={handleChange}
            onKeyDown={handleKeyDown}
            rows={1}
            placeholder="I am your Law / Press / Police Assistant — ask anything…"
            className="
              flex-1 resize-none bg-slate-50/80 backdrop-blur
              outline-none text-sm text-slate-900
              placeholder:text-slate-400
              max-h-36 leading-relaxed px-1
              transition-all
            "
          />

          {/* 🎙️ Mic */}
          <button className="relative group p-1">
            <span className="absolute inset-0 rounded-full bg-gradient-to-tr from-blue-500 to-purple-600 blur-md opacity-70"></span>
            <span className="relative flex items-center justify-center w-9 h-9 rounded-full bg-gradient-to-tr from-blue-500 to-purple-600 text-white text-sm">
              🎙️
            </span>
          </button>

          {/* Send */}
          <button
            onClick={handleSend}
            disabled={!message.trim()}
            className={`p-2 rounded-full transition ${
              message.trim()
                ? "bg-black text-white hover:bg-slate-800"
                : "bg-slate-300 text-slate-500 cursor-not-allowed"
            }`}
          >
            <Send size={16} />
          </button>
        </div>

        <p className="text-xs text-slate-400 text-center mt-2">
          Educational Use Only • Not a substitute for legal, police, or press services
        </p>
      </div>
    </div>
  );
}

































































































































































































































































// import React, { useRef } from "react";
// import { Plus, Send } from "lucide-react";

// export default function ChatInput({
//   onSendMessage,
//   message,
//   setMessage,
// }) {
//   const textareaRef = useRef(null);

//   const handleSend = () => {
//     if (!message.trim()) return;
//     onSendMessage(message);
//     setMessage("");
//     if (textareaRef.current) {
//       textareaRef.current.style.height = "auto";
//     }
//   };

//   const handleKeyDown = (e) => {
//     if (e.key === "Enter" && !e.shiftKey) {
//       e.preventDefault();
//       handleSend();
//     }
//   };

//   const handleChange = (e) => {
//     setMessage(e.target.value);
//     if (textareaRef.current) {
//       textareaRef.current.style.height = "auto";
//       textareaRef.current.style.height =
//         Math.min(textareaRef.current.scrollHeight, 140) + "px";
//     }
//   };

//   return (
//     <div className="bg-white border-t border-slate-200 py-4">
//       <div className="max-w-4xl mx-auto px-4">
//         <div className="flex items-end gap-3 bg-slate-100 rounded-2xl px-4 py-3 shadow-sm">
          
//           {/* Attach */}
//           <button className="text-slate-500 hover:text-slate-700 transition p-1">
//             <Plus size={18} />
//           </button>

//           {/* Input */}
//           <textarea
//             ref={textareaRef}
//             value={message}
//             onChange={handleChange}
//             onKeyDown={handleKeyDown}
//             rows={1}
//             placeholder="I am your Law / Press / Police Assistant — ask anything…"
//             className="
//               flex-1 resize-none bg-slate-50/80 backdrop-blur
//               outline-none text-sm text-slate-900
//               placeholder:text-slate-400
//               max-h-36 leading-relaxed px-1
//               focus:placeholder:text-slate-300
//               transition-all
//             "
//           />

//           {/* UNIC MIC */}
//           <button className="relative group p-1">
//             <span className="absolute inset-0 rounded-full bg-gradient-to-tr from-blue-500 to-purple-600 blur-md opacity-70"></span>
//             <span className="relative flex items-center justify-center w-9 h-9 rounded-full bg-gradient-to-tr from-blue-500 to-purple-600 text-white text-sm">
//               🎙️
//             </span>
//           </button>

//           {/* Send */}
//           <button
//             onClick={handleSend}
//             disabled={!message.trim()}
//             className={`p-2 rounded-full transition ${
//               message.trim()
//                 ? "bg-black text-white hover:bg-slate-800"
//                 : "bg-slate-300 text-slate-500 cursor-not-allowed"
//             }`}
//           >
//             <Send size={16} />
//           </button>
//         </div>

//         <p className="text-xs text-slate-400 text-center mt-2">
//           Free Research Preview • AI responses may be inaccurate
//         </p>
//       </div>
//     </div>
//   );
// }
