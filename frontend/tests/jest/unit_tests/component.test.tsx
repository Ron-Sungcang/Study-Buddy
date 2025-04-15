import { render, screen } from '@testing-library/react';
import { Welcome } from '../../../app/welcome/welcome';

// Just a simple starter UI unit test, will have to be changed since we not using this template for long
test('loads the welcome component and checks if the title "What\'s next?" is rendered', () => {
  render(<Welcome />);
  const titleElement = screen.getByText("What's next?");
  expect(titleElement).toBeInTheDocument();
});