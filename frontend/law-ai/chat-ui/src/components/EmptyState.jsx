import React from "react";
import {
  Gavel,
  BadgeCheck,
  Newspaper,
  MessagesSquare,
} from "lucide-react";

export default function EmptyState({ setInputText, onSendMessage }) {
  const suggestions = [
    {
      icon: Gavel,
      title: "Explain Law Sections",
      description: "Simple Way",
      style: "law",
    },
    {
      icon: Newspaper,
      title: "Write Press Articles",
      description: "Print | Electronic | Media",
      style: "press",
    },
    {
      icon: BadgeCheck,
      title: "Police Case Suggestions",
      description: "Investigation & summary",
      style: "police",
    },
    {
      icon: MessagesSquare,
      title: "General Discussion",
      description: "Law | Police | Press",
      style: "general",
    },
  ];

  const iconStyles = {
    law: "text-[#B89B2E] group-hover:text-[#D4AF37]",
    police:
      "text-blue-600 group-hover:text-blue-500 drop-shadow-[0_0_6px_rgba(37,99,235,0.35)]",
    press:
      "text-slate-600 group-hover:text-slate-800 group-hover:-translate-y-[1px]",
    general: "text-slate-700 group-hover:text-slate-900",
  };

  const handleCardClick = (title) => {
    // 1️⃣ Fill input
    setInputText(title);

    // 2️⃣ Auto-send (small delay for smooth UX)
    setTimeout(() => {
      onSendMessage(title);
    }, 100);
  };

  return (
    <div className="h-full flex flex-col items-center justify-center px-4">
      <div className="text-center mb-12">
        <h1 className="text-4xl font-semibold text-slate-900 mb-2">
          What's on the agenda today?
        </h1>
      </div>

      <div className="grid grid-cols-2 gap-4 w-full max-w-2xl">
        {suggestions.map((suggestion, index) => {
          const Icon = suggestion.icon;
          return (
            <button
              key={index}
              onClick={() => handleCardClick(suggestion.title)}
              className="
                p-5 rounded-xl
                bg-white
                border border-slate-200
                hover:bg-slate-50
                transition-all
                text-left
                group
              "
            >
              <Icon
                size={22}
                className={`mb-3 transition ${iconStyles[suggestion.style]}`}
              />

              <p className="text-sm font-medium text-slate-900 mb-1">
                {suggestion.title}
              </p>
              <p className="text-xs text-slate-600">
                {suggestion.description}
              </p>
            </button>
          );
        })}
      </div>
    </div>
  );
}














































































































































































































































// import React from "react";
// import {
//   Gavel,
//   BadgeCheck,
//   Newspaper,
//   MessagesSquare,
// } from "lucide-react";

// export default function EmptyState({ setInputText }) {
//   const suggestions = [
//     {
//       icon: Gavel,
//       title: "Explain Law Sections In Simple Way",
//       description: "Clear legal explanations",
//       style: "law",
//     },
//     {
//       icon: Newspaper,
//       title: "Write Press Articles",
//       description: "Print | Electronic | Media",
//       style: "press",
//     },
//     {
//       icon: BadgeCheck,
//       title: "Police Case Suggestions",
//       description: "Investigation & summary",
//       style: "police",
//     },
//     {
//       icon: MessagesSquare,
//       title: "General Discussion",
//       description: "Law | Police | Press",
//       style: "general",
//     },
//   ];

//   const iconStyles = {
//     law: "text-[#B89B2E] group-hover:text-[#D4AF37]",
//     police:
//       "text-blue-600 group-hover:text-blue-500 drop-shadow-[0_0_6px_rgba(37,99,235,0.35)]",
//     press:
//       "text-slate-600 group-hover:text-slate-800 group-hover:-translate-y-[1px]",
//     general: "text-slate-700 group-hover:text-slate-900",
//   };

//   return (
//     <div className="h-full flex flex-col items-center justify-center px-4">
//       <div className="text-center mb-12">
//         <h1 className="text-4xl font-semibold text-slate-900 mb-2">
//           What's on the agenda today?
//         </h1>
//         <p className="text-lg text-slate-600">
//           Start a conversation or explore what you can do
//         </p>
//       </div>

//       <div className="grid grid-cols-2 gap-4 w-full max-w-2xl">
//         {suggestions.map((suggestion, index) => {
//           const Icon = suggestion.icon;
//           return (
//             <button
//               key={index}
//               onClick={() => {
//                 // ⭐ MAIN FIX
//                 setInputText(suggestion.title);
//               }}
//               className="
//                 p-5 rounded-xl
//                 bg-white
//                 border border-slate-200
//                 hover:bg-slate-50
//                 transition-all
//                 text-left
//                 group
//               "
//             >
//               <Icon
//                 size={22}
//                 className={`mb-3 transition ${iconStyles[suggestion.style]}`}
//               />

//               <p className="text-sm font-medium text-slate-900 mb-1">
//                 {suggestion.title}
//               </p>
//               <p className="text-xs text-slate-600">
//                 {suggestion.description}
//               </p>
//             </button>
//           );
//         })}
//       </div>
//     </div>
//   );
// }
