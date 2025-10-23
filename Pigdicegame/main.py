"""Entry point for the Pig dice game application."""

from Game import Game


def main() -> None:
    """Instantiate the game and start its main loop."""
    g = Game()

    g.run()


if __name__ == "__main__":
    main()
