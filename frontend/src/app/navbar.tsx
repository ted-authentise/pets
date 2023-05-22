import { ThemeToggle } from "./theme-toggle";

export const Navbar = () => {
  return (
    <nav className="fixed top-0 w-screen h-16 flex flex-row justify-between">
      <h1>Dogs</h1>

      <ThemeToggle />
    </nav>
  );
};
