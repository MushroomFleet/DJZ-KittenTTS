#!/usr/bin/env python3
"""
KittenTTS Demonstration Script
=============================

A user-friendly demonstration of the KittenTTS text-to-speech model.
This script allows interactive text-to-speech generation with voice selection,
speed control, and file management.

Requirements:
- KittenTTS package installed
- Internet connection for model download (first run)
"""

import os
import sys
from datetime import datetime
from pathlib import Path

try:
    from kittentts import KittenTTS
except ImportError:
    print("❌ Error: KittenTTS package not found!")
    print("Please install it with:")
    print("pip install https://github.com/KittenML/KittenTTS/releases/download/0.1/kittentts-0.1.0-py3-none-any.whl")
    sys.exit(1)


class KittenTTSDemo:
    """Interactive demonstration class for KittenTTS."""
    
    def __init__(self):
        """Initialize the demo with model loading."""
        self.model = None
        self.voice_descriptions = {
            'expr-voice-2-m': 'Male Voice #2 - Expressive',
            'expr-voice-2-f': 'Female Voice #2 - Expressive', 
            'expr-voice-3-m': 'Male Voice #3 - Expressive',
            'expr-voice-3-f': 'Female Voice #3 - Expressive',
            'expr-voice-4-m': 'Male Voice #4 - Expressive',
            'expr-voice-4-f': 'Female Voice #4 - Expressive',
            'expr-voice-5-m': 'Male Voice #5 - Expressive',
            'expr-voice-5-f': 'Female Voice #5 - Expressive'
        }
        self.default_voice = 'expr-voice-2-f'
        self.output_dir = Path('generated_audio')
        
    def display_banner(self):
        """Display welcome banner."""
        print("=" * 60)
        print("🐱 KittenTTS Interactive Demo 🐱")
        print("=" * 60)
        print("Welcome to KittenTTS - Ultra-lightweight Text-to-Speech!")
        print("Features: 15M parameters • CPU-optimized • High quality")
        print("=" * 60)
        print()
        
    def load_model(self):
        """Load the KittenTTS model with progress indication."""
        print("🔄 Loading KittenTTS model...")
        print("   (This may take a moment on first run - downloading from Hugging Face)")
        
        try:
            self.model = KittenTTS("KittenML/kitten-tts-nano-0.1")
            print("✅ Model loaded successfully!")
            print()
        except Exception as e:
            print(f"❌ Error loading model: {e}")
            print("Please check your internet connection and try again.")
            sys.exit(1)
            
    def display_voices(self):
        """Display available voices with descriptions."""
        print("🎵 Available Voices:")
        print("-" * 40)
        
        for i, (voice_id, description) in enumerate(self.voice_descriptions.items(), 1):
            default_marker = " (default)" if voice_id == self.default_voice else ""
            print(f"{i:2d}. {voice_id:<15} - {description}{default_marker}")
        
        print("-" * 40)
        print()
        
    def get_user_input(self):
        """Get text input from user."""
        print("📝 Text Input:")
        print("Enter the text you want to convert to speech:")
        print("(Press Enter twice when done, or Ctrl+C to exit)")
        print()
        
        lines = []
        while True:
            try:
                line = input("> " if not lines else "  ")
                if line.strip() == "" and lines:
                    break
                lines.append(line)
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                sys.exit(0)
        
        text = "\n".join(lines).strip()
        if not text:
            print("❌ No text entered. Please try again.")
            return self.get_user_input()
            
        return text
        
    def get_voice_selection(self):
        """Get voice selection from user."""
        print("🎭 Voice Selection:")
        
        while True:
            try:
                choice = input(f"Choose voice (1-8, or Enter for default): ").strip()
                
                if choice == "":
                    return self.default_voice
                    
                choice_num = int(choice)
                if 1 <= choice_num <= 8:
                    voice_id = list(self.voice_descriptions.keys())[choice_num - 1]
                    print(f"Selected: {voice_id}")
                    return voice_id
                else:
                    print("❌ Please enter a number between 1 and 8.")
                    
            except ValueError:
                print("❌ Please enter a valid number.")
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                sys.exit(0)
                
    def get_speed_setting(self):
        """Get speed setting from user."""
        print("\n⚡ Speed Setting:")
        
        while True:
            try:
                speed_input = input("Speech speed (0.5-2.0, or Enter for 1.0): ").strip()
                
                if speed_input == "":
                    return 1.0
                    
                speed = float(speed_input)
                if 0.5 <= speed <= 2.0:
                    return speed
                else:
                    print("❌ Speed must be between 0.5 and 2.0")
                    
            except ValueError:
                print("❌ Please enter a valid number.")
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                sys.exit(0)
                
    def get_output_filename(self, text_preview):
        """Get output filename from user."""
        # Create output directory if it doesn't exist
        self.output_dir.mkdir(exist_ok=True)
        
        # Generate default filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        text_slug = "".join(c for c in text_preview[:20] if c.isalnum() or c in (' ', '-', '_')).strip()
        text_slug = "_".join(text_slug.split())
        default_filename = f"tts_{timestamp}_{text_slug}.wav"
        
        print(f"\n💾 Output File:")
        print(f"Default: {self.output_dir / default_filename}")
        
        while True:
            try:
                filename_input = input("Custom filename (or Enter for default): ").strip()
                
                if filename_input == "":
                    filepath = self.output_dir / default_filename
                else:
                    # Ensure .wav extension
                    if not filename_input.endswith('.wav'):
                        filename_input += '.wav'
                    filepath = self.output_dir / filename_input
                
                # Check if file exists
                if filepath.exists():
                    overwrite = input(f"File exists. Overwrite? (y/N): ").strip().lower()
                    if overwrite != 'y':
                        continue
                        
                return str(filepath)
                
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                sys.exit(0)
                
    def generate_audio(self, text, voice, speed, output_path):
        """Generate audio and save to file."""
        print(f"\n🎙️  Generating speech...")
        print(f"   Text: {text[:50]}{'...' if len(text) > 50 else ''}")
        print(f"   Voice: {voice}")
        print(f"   Speed: {speed}x")
        print(f"   Output: {output_path}")
        print()
        
        try:
            # Generate audio
            self.model.generate_to_file(
                text=text,
                output_path=output_path,
                voice=voice,
                speed=speed
            )
            
            # Check file was created successfully
            if os.path.exists(output_path):
                file_size = os.path.getsize(output_path)
                print(f"✅ Audio generated successfully!")
                print(f"   File: {output_path}")
                print(f"   Size: {file_size:,} bytes")
                return True
            else:
                print("❌ Error: Output file was not created.")
                return False
                
        except Exception as e:
            print(f"❌ Error generating audio: {e}")
            return False
            
    def run_demo_session(self):
        """Run a single demo session."""
        # Get user inputs
        text = self.get_user_input()
        print(f"\n📋 Text: {text[:100]}{'...' if len(text) > 100 else ''}")
        
        self.display_voices()
        voice = self.get_voice_selection()
        
        speed = self.get_speed_setting()
        
        output_path = self.get_output_filename(text)
        
        # Generate audio
        success = self.generate_audio(text, voice, speed, output_path)
        
        return success
        
    def run(self):
        """Run the interactive demo."""
        self.display_banner()
        self.load_model()
        
        session_count = 0
        
        while True:
            session_count += 1
            print(f"\n{'='*20} Session {session_count} {'='*20}")
            
            success = self.run_demo_session()
            
            if success:
                print(f"\n🎉 Session {session_count} completed!")
            else:
                print(f"\n😞 Session {session_count} failed.")
            
            # Ask if user wants to continue
            print("\n" + "="*60)
            try:
                continue_choice = input("Generate another audio file? (Y/n): ").strip().lower()
                if continue_choice in ('n', 'no'):
                    break
            except KeyboardInterrupt:
                break
        
        print(f"\n👋 Demo completed! Generated {session_count} audio file(s).")
        print(f"Audio files saved in: {self.output_dir.absolute()}")


def main():
    """Main entry point."""
    demo = KittenTTSDemo()
    demo.run()


if __name__ == "__main__":
    main()
