import React from "react";

export default function MessageBubble({ message }) {
  const isUser = message.role === "user";

  const renderContent = () => {
    // Assistant response object handling
    if (typeof message.content === "object" && message.content !== null) {
      return (
        <div className="space-y-2">
          {message.content.reply && (
            <p className="whitespace-pre-line">
              {message.content.reply}
            </p>
          )}

          {message.content.confidence && (
            <p className="text-xs text-slate-500">
              Confidence: {message.content.confidence}%
            </p>
          )}
        </div>
      );
    }

    // Normal string (user message)
    return message.content;
  };

  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"}`}>
      <div
        className={`max-w-xl lg:max-w-2xl px-4 py-3 text-sm leading-relaxed shadow-sm
          ${
            isUser
              ? "bg-gradient-to-tr from-blue-500 to-blue-600 text-white rounded-2xl rounded-br-md"
              : "bg-white text-slate-900 border border-slate-200 rounded-2xl rounded-bl-md"
          }`}
      >
        {renderContent()}
      </div>
    </div>
  );
}























































































// import React from "react";

// export default function MessageBubble({ message }) {
//   const isUser = message.role === "user";

//   return (
//     <div className={`flex ${isUser ? "justify-end" : "justify-start"}`}>
//       <div
//         className={`max-w-xl lg:max-w-2xl px-4 py-3 text-sm leading-relaxed shadow-sm
//           ${
//             isUser
//               ? "bg-gradient-to-tr from-blue-500 to-blue-600 text-white rounded-2xl rounded-br-md"
//               : "bg-white text-slate-900 border border-slate-200 rounded-2xl rounded-bl-md"
//           }`}
//       >
//         {message.content}
//       </div>
//     </div>
//   );
// }
