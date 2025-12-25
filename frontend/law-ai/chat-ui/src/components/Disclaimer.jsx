import React from "react";

export default function Disclaimer({ onAccept }) {
  return (
    <div className="h-screen flex items-center justify-center bg-slate-50 px-6">
      <div className="max-w-xl bg-white rounded-2xl shadow-lg p-8 text-center space-y-6">
        
        <h1 className="text-2xl font-semibold text-slate-900">
          Important Notice
        </h1>

        <p className="text-slate-600 text-sm leading-relaxed">
          This AI assistant is provided <b>only for knowledge and educational purposes</b>.
          <br /><br />
          It does <b>not replace</b> professional advice from:
        </p>

        <ul className="text-left text-slate-600 text-sm list-disc ml-6">
          <li>Lawyers / Legal professionals</li>
          <li>Police authorities</li>
          <li>Press / Media experts</li>
        </ul>

        <p className="text-xs text-slate-500">
          Always consult official authorities for real-world decisions.
        </p>

        <button
          onClick={onAccept}
          className="w-full bg-black text-white py-3 rounded-xl font-medium hover:bg-slate-800 transition"
        >
          I Understand & Accept
        </button>
      </div>
    </div>
  );
}
