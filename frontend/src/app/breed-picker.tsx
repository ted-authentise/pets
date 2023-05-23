import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import breeds from "@/breeds.json";

interface Props {
  value: string;
  setValue: (val: string) => void;
}
export const BreedPicker: React.FC<Props> = ({ value, setValue }) => {
  return (
    <Select value={value} onValueChange={setValue}>
      <SelectTrigger className="w-72">
        <SelectValue />
      </SelectTrigger>
      <SelectContent className="h-40">
        <SelectItem value="">All Breeds</SelectItem>
        {breeds.map((breed) => (
          <SelectItem value={breed.path}>{toTitle(breed.name)}</SelectItem>
        ))}
      </SelectContent>
    </Select>
  );
};

const toTitle = (str: string): string => {
  return str
    .split(" ")
    .map((substr) => substr.charAt(0).toUpperCase() + substr.slice(1))
    .join(" ");
};
