"use client";

import { Button } from "@/components/ui/button";
import { Moon, Sun } from "lucide-react";
import { useEffect, useState } from "react";

type Theme = "light" | "dark";

const useTheme = () => {
  const getInitialTheme = (): Theme => {
    if (localStorage.theme === "light" || localStorage.theme === "dark") {
      return localStorage.theme;
    }
    return window.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark"
      : "light";
  };

  const [theme, setTheme] = useState(getInitialTheme());

  const toggleTheme = () => {
    const newTheme = theme === "light" ? "dark" : "light";

    const rootEl = window.document.documentElement;
    rootEl.classList.remove(theme);
    rootEl.classList.add(newTheme);

    setTheme(newTheme);
    localStorage.setItem("theme", newTheme);
  };

  return { theme, toggleTheme };
};

export const ThemeToggle = () => {
  const { theme, toggleTheme } = useTheme();

  useEffect(() => {
    window.document.documentElement.classList.add(theme);
  }, []);

  return (
    <Button onClick={() => toggleTheme()}>
      {theme === "dark" ? <Moon /> : <Sun />}
    </Button>
  );
};
