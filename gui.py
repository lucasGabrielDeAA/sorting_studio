"""
Modern Desktop GUI for Sorting Algorithms.
Built with pure Python Tkinter with custom-rendered canvas UI widgets
for 100% cross-platform color fidelity and high-contrast modern aesthetics.
Algorithms are cleanly grouped by their theoretical complexity in dedicated columns.
"""

import sys
import random
import tkinter as tk
from tkinter import messagebox

from helpers import calculate_execution_time
from sorting.bubble_sort import bubble_sort
from sorting.selection_sort import selection_sort
from sorting.insertion_sort import insertion_sort
from sorting.cocktail_shaker_sort import cocktail_shaker_sort
from sorting.gnome_sort import gnome_sort
from sorting.comb_sort import comb_sort
from sorting.shell_sort import shell_sort
from sorting.merge_sort import merge_sort
from sorting.quick_sort import quick_sort
from sorting.heap_sort import heap_sort
from sorting.tim_sort import tim_sort
from sorting.counting_sort import counting_sort
from sorting.radix_sort import radix_sort
from sorting.bucket_sort import bucket_sort


# ----------------------------------------------------------------------
# Design System & Theme Constants
# ----------------------------------------------------------------------
THEME = {
    "bg_root": "#0B0F19",       # Deep Obsidian
    "bg_card": "#151D2F",       # Card background
    "bg_card_inner": "#0E1524", # Inner well background
    "bg_column": "#121A2B",     # Column card background
    "bg_hover": "#1E293B",      # Card hover
    "border": "#283548",        # Subtle border
    "border_focus": "#6366F1",  # Accent focus border
    "text_main": "#F8FAFC",     # Bright primary text (High Contrast White)
    "text_muted": "#94A3B8",    # Secondary text (Light Slate)
    "text_dim": "#64748B",      # Dim helper text
    "accent_primary": "#6366F1",# Indigo
    "accent_secondary": "#8B5CF6", # Purple
    "success": "#10B981",       # Emerald green
    "warning": "#F59E0B",       # Amber
    "danger": "#EF4444",        # Red
    "font_family": "SF Pro Display, Helvetica Neue, Segoe UI, Arial, sans-serif",
}

# ----------------------------------------------------------------------
# Algorithm Definitions & Complexity Groupings
# ----------------------------------------------------------------------
ALGORITHMS = {
    # --- Quadratic O(n²) ---
    "Bubble Sort": {
        "func": bubble_sort,
        "complexity": "O(n²)",
        "color": "#E11D48",       # Vibrant Rose
        "hover": "#F43F5E",
        "category": "quadratic",
        "desc": "Compares adjacent elements and swaps them if in the wrong order.",
    },
    "Selection Sort": {
        "func": selection_sort,
        "complexity": "O(n²)",
        "color": "#EA580C",       # Vibrant Orange
        "hover": "#F97316",
        "category": "quadratic",
        "desc": "Repeatedly selects the minimum element from the unsorted part.",
    },
    "Insertion Sort": {
        "func": insertion_sort,
        "complexity": "O(n²)",
        "color": "#D97706",       # Amber
        "hover": "#F59E0B",
        "category": "quadratic",
        "desc": "Builds the sorted array one item at a time by insertion.",
    },
    "Cocktail Sort": {
        "func": cocktail_shaker_sort,
        "complexity": "O(n²)",
        "color": "#BE123C",       # Crimson
        "hover": "#E11D48",
        "category": "quadratic",
        "desc": "Bidirectional bubble sort traversing back and forth.",
    },
    "Gnome Sort": {
        "func": gnome_sort,
        "complexity": "O(n²)",
        "color": "#9A3412",       # Warm Rust
        "hover": "#C2410C",
        "category": "quadratic",
        "desc": "Swaps backward like insertion sort then moves forward.",
    },

    # --- Log-Linear & Sub-Quadratic O(n log n) ---
    "Merge Sort": {
        "func": merge_sort,
        "complexity": "O(n log n)",
        "color": "#0284C7",       # Sky Blue
        "hover": "#0EA5E9",
        "category": "log_linear",
        "desc": "Divides array into halves, sorts recursively, then merges.",
    },
    "Quick Sort": {
        "func": quick_sort,
        "complexity": "O(n log n)",
        "color": "#7C3AED",       # Deep Purple / Violet
        "hover": "#8B5CF6",
        "category": "log_linear",
        "desc": "Partitions around a pivot and sorts partitions recursively.",
    },
    "Heap Sort": {
        "func": heap_sort,
        "complexity": "O(n log n)",
        "color": "#059669",       # Emerald Green
        "hover": "#10B981",
        "category": "log_linear",
        "desc": "Transforms array into a max heap, then extracts max repeatedly.",
    },
    "Tim Sort": {
        "func": tim_sort,
        "complexity": "O(n log n)",
        "color": "#4F46E5",       # Indigo
        "hover": "#6366F1",
        "category": "log_linear",
        "desc": "Hybrid algorithm derived from merge sort and insertion sort.",
    },
    "Shell Sort": {
        "func": shell_sort,
        "complexity": "O(n log² n)",
        "color": "#2563EB",       # Royal Blue
        "hover": "#3B82F6",
        "category": "log_linear",
        "desc": "Generalization of insertion sort with diminishing gap intervals.",
    },
    "Comb Sort": {
        "func": comb_sort,
        "complexity": "O(n log n)",
        "color": "#9333EA",       # Vibrant Purple
        "hover": "#A855F7",
        "category": "log_linear",
        "desc": "Improvement on bubble sort using a shrink gap factor (1.3).",
    },

    # --- Linear / Distribution O(n + k) ---
    "Counting Sort": {
        "func": counting_sort,
        "complexity": "O(n + k)",
        "color": "#0891B2",       # Vibrant Cyan
        "hover": "#06B6D4",
        "category": "linear",
        "desc": "Counts occurrences of each value and reconstructs sorted array.",
    },
    "Radix Sort": {
        "func": radix_sort,
        "complexity": "O(n + k)",
        "color": "#D946EF",       # Vibrant Fuchsia / Magenta
        "hover": "#E879F9",
        "category": "linear",
        "desc": "Sorts integers digit by digit from least to most significant.",
    },
    "Bucket Sort": {
        "func": bucket_sort,
        "complexity": "O(n + k)",
        "color": "#0D9488",       # Deep Teal
        "hover": "#14B8A6",
        "category": "linear",
        "desc": "Distributes elements into buckets then sorts each bucket.",
    },
}

COMPLEXITY_COLUMNS = [
    {
        "id": "quadratic",
        "title": "QUADRATIC",
        "badge": "O(n²)",
        "badge_bg": "#451A03",
        "badge_fg": "#F59E0B",
        "accent_color": "#D97706",
        "algos": ["Bubble Sort", "Selection Sort", "Insertion Sort", "Cocktail Sort", "Gnome Sort"],
    },
    {
        "id": "log_linear",
        "title": "LOG-LINEAR",
        "badge": "O(n log n)",
        "badge_bg": "#1E1B4B",
        "badge_fg": "#A5B4FC",
        "accent_color": "#6366F1",
        "algos": ["Merge Sort", "Quick Sort", "Heap Sort", "Tim Sort", "Shell Sort", "Comb Sort"],
    },
    {
        "id": "linear",
        "title": "LINEAR / DISTRIBUTION",
        "badge": "O(n + k)",
        "badge_bg": "#164E63",
        "badge_fg": "#67E8F9",
        "accent_color": "#0891B2",
        "algos": ["Counting Sort", "Radix Sort", "Bucket Sort"],
    },
]


# ----------------------------------------------------------------------
# Modern Custom UI Components (Canvas-Rendered)
# ----------------------------------------------------------------------
class RoundedCanvasButton(tk.Canvas):
    """
    Modern smooth rounded button with hover animations, badges, and
    guaranteed high-contrast text across all operating systems.
    """

    def __init__(
        self,
        parent,
        text,
        command=None,
        badge="",
        bg_color="#6366F1",
        hover_color="#818CF8",
        text_color="#FFFFFF",
        badge_color="#FFFFFF",
        badge_bg="#0F172A",
        radius=7,
        height=32,
        width=None,
        font_size=9,
        bold=True,
        border_color="",
        canvas_bg=THEME["bg_column"],
        **kwargs,
    ):
        super().__init__(
            parent,
            bg=canvas_bg,
            highlightthickness=0,
            cursor="pointinghand" if sys.platform == "darwin" else "hand2",
            height=height,
            **kwargs,
        )
        self.text = text
        self.badge = badge
        self.command = command
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.text_color = text_color
        self.badge_color = badge_color
        self.badge_bg = badge_bg
        self.radius = radius
        self.btn_height = height
        self.btn_width = width
        self.font_size = font_size
        self.bold = bold
        self.border_color = border_color
        self.is_hovered = False
        self.is_pressed = False

        self.bind("<Configure>", self._on_resize)
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
        self.bind("<Button-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _draw_rounded_rect(self, x1, y1, x2, y2, r, fill, outline=""):
        points = [
            x1 + r, y1,
            x2 - r, y1,
            x2, y1,
            x2, y1 + r,
            x2, y2 - r,
            x2, y2,
            x2 - r, y2,
            x1 + r, y2,
            x1, y2,
            x1, y2 - r,
            x1, y1 + r,
            x1, y1,
        ]
        return self.create_polygon(points, fill=fill, outline=outline, smooth=True)

    def redraw(self):
        self.delete("all")
        w = self.winfo_width()
        h = self.winfo_height()
        if w <= 1 or h <= 1:
            w = self.btn_width or 160
            h = self.btn_height

        fill = self.hover_color if self.is_hovered else self.bg_color
        if self.is_pressed:
            fill = self._adjust_brightness(fill, 0.8)

        outline = self.border_color if self.border_color else ""
        self._draw_rounded_rect(1, 1, w - 1, h - 1, self.radius, fill=fill, outline=outline)

        weight = "bold" if self.bold else "normal"
        font_main = (THEME["font_family"], self.font_size, weight)

        if self.badge:
            badge_font = (THEME["font_family"], max(8, self.font_size - 2), "bold")
            self.create_text(
                10,
                h / 2,
                text=self.text,
                fill=self.text_color,
                font=font_main,
                anchor="w",
            )
            badge_text_w = len(self.badge) * 6 + 10
            bx2 = w - 8
            bx1 = bx2 - badge_text_w
            by1 = h / 2 - 8
            by2 = h / 2 + 8
            badge_fill = self._adjust_brightness(fill, 0.65)
            self._draw_rounded_rect(bx1, by1, bx2, by2, 4, fill=badge_fill)
            self.create_text(
                (bx1 + bx2) / 2,
                h / 2,
                text=self.badge,
                fill=self.badge_color,
                font=badge_font,
                anchor="center",
            )
        else:
            self.create_text(
                w / 2,
                h / 2,
                text=self.text,
                fill=self.text_color,
                font=font_main,
                anchor="center",
            )

    def _adjust_brightness(self, hex_color, factor):
        hex_color = hex_color.lstrip("#")
        if len(hex_color) != 6:
            return hex_color
        r, g, b = (int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        r = max(0, min(255, int(r * factor)))
        g = max(0, min(255, int(g * factor)))
        b = max(0, min(255, int(b * factor)))
        return f"#{r:02x}{g:02x}{b:02x}"

    def _on_resize(self, event):
        self.redraw()

    def _on_enter(self, event):
        self.is_hovered = True
        self.redraw()

    def _on_leave(self, event):
        self.is_hovered = False
        self.is_pressed = False
        self.redraw()

    def _on_press(self, event):
        self.is_pressed = True
        self.redraw()

    def _on_release(self, event):
        if self.is_pressed:
            self.is_pressed = False
            self.redraw()
            if self.command:
                self.command()


class PillButton(tk.Canvas):
    """
    Compact modern pill button used for quick presets and secondary actions.
    Uses custom canvas drawing so text and backgrounds are crystal clear on macOS/Windows.
    """

    def __init__(
        self,
        parent,
        text,
        command=None,
        bg_color="#1E293B",
        hover_color="#334155",
        text_color="#F8FAFC",
        border_color="#334155",
        font_size=9,
        bold=True,
        radius=6,
        height=28,
        width=None,
        canvas_bg=THEME["bg_card"],
        **kwargs,
    ):
        calc_w = width if width else (len(text) * 7 + 24)
        super().__init__(
            parent,
            bg=canvas_bg,
            highlightthickness=0,
            cursor="pointinghand" if sys.platform == "darwin" else "hand2",
            height=height,
            width=calc_w,
            **kwargs,
        )
        self.text = text
        self.command = command
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.text_color = text_color
        self.border_color = border_color
        self.font_size = font_size
        self.bold = bold
        self.radius = radius
        self.btn_height = height
        self.btn_width = calc_w
        self.is_hovered = False
        self.is_pressed = False

        self.bind("<Configure>", lambda e: self.redraw())
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
        self.bind("<Button-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        self.redraw()

    def _draw_rounded_rect(self, x1, y1, x2, y2, r, fill, outline=""):
        points = [
            x1 + r, y1,
            x2 - r, y1,
            x2, y1,
            x2, y1 + r,
            x2, y2 - r,
            x2, y2,
            x2 - r, y2,
            x1 + r, y2,
            x1, y2,
            x1, y2 - r,
            x1, y1 + r,
            x1, y1,
        ]
        return self.create_polygon(points, fill=fill, outline=outline, smooth=True)

    def redraw(self):
        self.delete("all")
        w = self.winfo_width()
        h = self.winfo_height()
        if w <= 1 or h <= 1:
            w = self.btn_width
            h = self.btn_height

        fill = self.hover_color if self.is_hovered else self.bg_color
        if self.is_pressed:
            fill = "#475569"

        self._draw_rounded_rect(1, 1, w - 1, h - 1, self.radius, fill=fill, outline=self.border_color)

        weight = "bold" if self.bold else "normal"
        self.create_text(
            w / 2,
            h / 2,
            text=self.text,
            fill=self.text_color,
            font=(THEME["font_family"], self.font_size, weight),
            anchor="center",
        )

    def _on_enter(self, event):
        self.is_hovered = True
        self.redraw()

    def _on_leave(self, event):
        self.is_hovered = False
        self.is_pressed = False
        self.redraw()

    def _on_press(self, event):
        self.is_pressed = True
        self.redraw()

    def _on_release(self, event):
        if self.is_pressed:
            self.is_pressed = False
            self.redraw()
            if self.command:
                self.command()


class ArrayBarVisualizer(tk.Canvas):
    """Modern interactive bar visualizer canvas showing numbers before and after sorting."""

    def __init__(self, parent, height=85, **kwargs):
        super().__init__(
            parent,
            bg=THEME["bg_card_inner"],
            highlightthickness=1,
            highlightbackground=THEME["border"],
            height=height,
            **kwargs,
        )
        self.current_array = []
        self.is_sorted_state = False
        self.bind("<Configure>", lambda e: self.render())

    def update_data(self, array, is_sorted=False):
        self.current_array = list(array)
        self.is_sorted_state = is_sorted
        self.render()

    def render(self):
        self.delete("all")
        w = self.winfo_width()
        h = self.winfo_height()
        if w <= 10 or h <= 10:
            return

        if not self.current_array:
            self.create_text(
                w / 2,
                h / 2,
                text="📊 Array visualization will appear here upon typing numbers or sorting",
                fill=THEME["text_dim"],
                font=(THEME["font_family"], 11, "italic"),
            )
            return

        n = len(self.current_array)
        min_val = min(self.current_array)
        max_val = max(self.current_array)
        range_val = max_val - min_val if max_val != min_val else 1

        padding_x = 18
        padding_y = 14
        avail_w = w - (padding_x * 2)
        avail_h = h - (padding_y * 2)

        gap = max(2, min(6, int(avail_w / (n * 3)))) if n < 50 else 1
        bar_w = max(1.5, (avail_w - (gap * (n - 1))) / n)

        for i, val in enumerate(self.current_array):
            prop = (val - min_val) / range_val
            bar_h = max(4, prop * avail_h)

            x1 = padding_x + i * (bar_w + gap)
            x2 = x1 + bar_w
            y2 = h - padding_y
            y1 = y2 - bar_h

            if self.is_sorted_state:
                fill_color = "#10B981" if i % 2 == 0 else "#06B6D4"
            else:
                fill_color = "#6366F1" if i % 2 == 0 else "#8B5CF6"

            self.create_rectangle(
                x1, y1, x2, y2,
                fill=fill_color,
                outline="",
            )

            if n <= 16:
                self.create_text(
                    (x1 + x2) / 2,
                    y1 - 7,
                    text=str(val),
                    fill=THEME["text_muted"],
                    font=(THEME["font_family"], 9, "bold"),
                )


# ----------------------------------------------------------------------
# Main Application Window
# ----------------------------------------------------------------------
class SortsApp(tk.Tk):
    """State of the art Modern GUI for Sorting Algorithms & Benchmarking."""

    def __init__(self, initial_list=None):
        super().__init__()
        self.title("Sort Algorithms — Visualizer & Benchmark Suite")
        self.geometry("1060x890")
        self.minsize(960, 800)
        self.configure(bg=THEME["bg_root"])

        self.initial_sample = initial_list if initial_list else [120, 30, 45, 99, 12, 5]
        self.last_sorted_result = None
        self.last_execution_time = 0.0
        self.last_algorithm_name = "None"

        self._create_layout()
        self._set_input_list(self.initial_sample)

    def _create_layout(self):
        self.main_frame = tk.Frame(self, bg=THEME["bg_root"], padx=22, pady=14)
        self.main_frame.pack(fill="both", expand=True)

        self._build_header(self.main_frame)
        self._build_input_card(self.main_frame)
        self._build_complexity_columns_card(self.main_frame)
        self._build_visualizer_card(self.main_frame)
        self._build_bottom_metrics_dashboard(self.main_frame)

    def _build_header(self, parent):
        header_frame = tk.Frame(parent, bg=THEME["bg_root"])
        header_frame.pack(fill="x", pady=(0, 8))

        left_box = tk.Frame(header_frame, bg=THEME["bg_root"])
        left_box.pack(side="left")

        title_lbl = tk.Label(
            left_box,
            text="⚡ Sorting Algorithm Studio",
            font=(THEME["font_family"], 18, "bold"),
            fg=THEME["text_main"],
            bg=THEME["bg_root"],
        )
        title_lbl.pack(anchor="w")

        subtitle_lbl = tk.Label(
            left_box,
            text="14 Algorithms categorized by time complexity: O(n²), O(n log n), and O(n + k)",
            font=(THEME["font_family"], 10),
            fg=THEME["text_muted"],
            bg=THEME["bg_root"],
        )
        subtitle_lbl.pack(anchor="w", pady=(1, 0))

        self.status_badge = tk.Label(
            header_frame,
            text="● SYSTEM READY",
            font=(THEME["font_family"], 9, "bold"),
            fg=THEME["success"],
            bg="#064E3B",
            padx=10,
            pady=4,
            relief="flat",
        )
        self.status_badge.pack(side="right", pady=2)

    def _build_input_card(self, parent):
        card = tk.Frame(
            parent,
            bg=THEME["bg_card"],
            highlightthickness=1,
            highlightbackground=THEME["border"],
            padx=14,
            pady=10,
        )
        card.pack(fill="x", pady=(0, 8))

        lbl_row = tk.Frame(card, bg=THEME["bg_card"])
        lbl_row.pack(fill="x", pady=(0, 4))

        tk.Label(
            lbl_row,
            text="INPUT ARRAY / NUMBERS TO SORT",
            font=(THEME["font_family"], 9, "bold"),
            fg=THEME["accent_primary"],
            bg=THEME["bg_card"],
        ).pack(side="left")

        self.count_badge = tk.Label(
            lbl_row,
            text="0 elements",
            font=(THEME["font_family"], 8, "bold"),
            fg=THEME["text_muted"],
            bg=THEME["bg_card_inner"],
            padx=8,
            pady=2,
        )
        self.count_badge.pack(side="right")

        entry_container = tk.Frame(
            card,
            bg=THEME["bg_card_inner"],
            highlightthickness=1,
            highlightbackground=THEME["border"],
            padx=8,
            pady=5,
        )
        entry_container.pack(fill="x", pady=(0, 6))

        self.input_entry = tk.Entry(
            entry_container,
            font=(THEME["font_family"], 12),
            bg=THEME["bg_card_inner"],
            fg=THEME["text_main"],
            insertbackground=THEME["accent_primary"],
            relief="flat",
            highlightthickness=0,
        )
        self.input_entry.pack(fill="x", side="left", expand=True)
        self.input_entry.bind("<KeyRelease>", self._on_entry_changed)
        self.input_entry.bind("<Return>", lambda e: self.run_algorithm("Quick Sort"))

        preset_row = tk.Frame(card, bg=THEME["bg_card"])
        preset_row.pack(fill="x")

        tk.Label(
            preset_row,
            text="Presets:",
            font=(THEME["font_family"], 8, "bold"),
            fg=THEME["text_muted"],
            bg=THEME["bg_card"],
        ).pack(side="left", padx=(0, 6))

        presets = [
            ("Default (6)", lambda: self._set_input_list([120, 30, 45, 99, 12, 5]), "#1E293B", "#38BDF8"),
            ("Random 20", lambda: self._set_input_list([random.randint(1, 100) for _ in range(20)]), "#1E293B", "#F8FAFC"),
            ("Reverse 15", lambda: self._set_input_list(list(range(95, 20, -5))), "#1E293B", "#F8FAFC"),
            ("Nearly Sorted 25", self._generate_nearly_sorted, "#1E293B", "#F8FAFC"),
            ("Random 100", lambda: self._set_input_list([random.randint(1, 500) for _ in range(100)]), "#1E293B", "#F8FAFC"),
            ("Clear", self._clear_input, "#3B1828", "#FB7185"),
        ]

        for title, cmd, bg_col, text_col in presets:
            btn = PillButton(
                preset_row,
                text=title,
                command=cmd,
                bg_color=bg_col,
                hover_color="#334155" if bg_col != "#3B1828" else "#501D38",
                text_color=text_col,
                border_color="#334155" if bg_col != "#3B1828" else "#881337",
                canvas_bg=THEME["bg_card"],
                font_size=8,
                bold=True,
                height=24,
            )
            btn.pack(side="left", padx=2)

    def _build_complexity_columns_card(self, parent):
        """
        Builds the 3 dedicated complexity columns for quadratic, log-linear,
        and linear/distribution algorithms.
        """
        card = tk.Frame(
            parent,
            bg=THEME["bg_card"],
            highlightthickness=1,
            highlightbackground=THEME["border"],
            padx=14,
            pady=10,
        )
        card.pack(fill="x", pady=(0, 8))

        top_row = tk.Frame(card, bg=THEME["bg_card"])
        top_row.pack(fill="x", pady=(0, 8))

        tk.Label(
            top_row,
            text="ALGORITHMS GROUPED BY COMPLEXITY",
            font=(THEME["font_family"], 9, "bold"),
            fg=THEME["accent_primary"],
            bg=THEME["bg_card"],
        ).pack(side="left")

        bench_btn = RoundedCanvasButton(
            top_row,
            text=f"⚡ Run Benchmark (All {len(ALGORITHMS)})",
            command=self.run_benchmark_all,
            bg_color="#4F46E5",
            hover_color="#6366F1",
            text_color="#FFFFFF",
            radius=6,
            height=26,
            width=190,
            font_size=9,
            bold=True,
            canvas_bg=THEME["bg_card"],
        )
        bench_btn.pack(side="right")

        # 3 Side-by-side Complexity Columns
        columns_container = tk.Frame(card, bg=THEME["bg_card"])
        columns_container.pack(fill="x")
        columns_container.columnconfigure((0, 1, 2), weight=1, uniform="complexity_cols")

        for col_idx, col_data in enumerate(COMPLEXITY_COLUMNS):
            col_frame = tk.Frame(
                columns_container,
                bg=THEME["bg_column"],
                highlightthickness=1,
                highlightbackground=THEME["border"],
                padx=8,
                pady=8,
            )
            col_frame.grid(row=0, column=col_idx, padx=4, sticky="nsew")

            # Column Header with Title & Complexity Badge
            col_header = tk.Frame(col_frame, bg=THEME["bg_column"])
            col_header.pack(fill="x", pady=(0, 6))

            tk.Label(
                col_header,
                text=col_data["title"],
                font=(THEME["font_family"], 9, "bold"),
                fg=col_data["accent_color"],
                bg=THEME["bg_column"],
            ).pack(side="left")

            tk.Label(
                col_header,
                text=col_data["badge"],
                font=(THEME["font_family"], 8, "bold"),
                fg=col_data["badge_fg"],
                bg=col_data["badge_bg"],
                padx=6,
                pady=1,
            ).pack(side="right")

            # Buttons inside this complexity column
            for algo_name in col_data["algos"]:
                meta = ALGORITHMS[algo_name]
                btn = RoundedCanvasButton(
                    col_frame,
                    text=algo_name,
                    badge="",
                    bg_color=meta["color"],
                    hover_color=meta["hover"],
                    text_color="#FFFFFF",
                    radius=6,
                    height=30,
                    font_size=10,
                    bold=True,
                    canvas_bg=THEME["bg_column"],
                    command=lambda n=algo_name: self.run_algorithm(n),
                )
                btn.pack(fill="x", pady=2)

    def _build_visualizer_card(self, parent):
        card = tk.Frame(
            parent,
            bg=THEME["bg_card"],
            highlightthickness=1,
            highlightbackground=THEME["border"],
            padx=14,
            pady=8,
        )
        card.pack(fill="both", expand=True, pady=(0, 8))

        v_head = tk.Frame(card, bg=THEME["bg_card"])
        v_head.pack(fill="x", pady=(0, 4))

        tk.Label(
            v_head,
            text="ARRAY VISUALIZATION & SORTED RESULT",
            font=(THEME["font_family"], 9, "bold"),
            fg=THEME["accent_primary"],
            bg=THEME["bg_card"],
        ).pack(side="left")

        self.sort_state_label = tk.Label(
            v_head,
            text="Unsorted Input",
            font=(THEME["font_family"], 8, "bold"),
            fg=THEME["text_muted"],
            bg=THEME["bg_card_inner"],
            padx=8,
            pady=1,
        )
        self.sort_state_label.pack(side="right")

        self.visualizer = ArrayBarVisualizer(card, height=75)
        self.visualizer.pack(fill="x", pady=(0, 6))

        result_box = tk.Frame(
            card,
            bg=THEME["bg_card_inner"],
            highlightthickness=1,
            highlightbackground=THEME["border"],
            padx=8,
            pady=4,
        )
        result_box.pack(fill="x")

        tk.Label(
            result_box,
            text="Result:",
            font=(THEME["font_family"], 9, "bold"),
            fg=THEME["text_muted"],
            bg=THEME["bg_card_inner"],
        ).pack(side="left", padx=(0, 6))

        self.result_display = tk.Entry(
            result_box,
            font=(THEME["font_family"], 11),
            bg=THEME["bg_card_inner"],
            fg="#34D399",
            relief="flat",
            highlightthickness=0,
        )
        self.result_display.pack(side="left", fill="x", expand=True)
        self.result_display.insert(0, "Click an algorithm button above to sort")
        self.result_display.config(state="readonly")

        copy_btn = PillButton(
            result_box,
            text="📋 Copy",
            command=self._copy_result_to_clipboard,
            bg_color="#1E293B",
            hover_color="#334155",
            text_color="#38BDF8",
            border_color="#38BDF8",
            canvas_bg=THEME["bg_card_inner"],
            font_size=8,
            bold=True,
            height=22,
        )
        copy_btn.pack(side="right", padx=(4, 0))

    def _build_bottom_metrics_dashboard(self, parent):
        card = tk.Frame(
            parent,
            bg="#111C33",
            highlightthickness=1,
            highlightbackground="#3B82F6",
            padx=16,
            pady=8,
        )
        card.pack(fill="x")

        top_metric = tk.Frame(card, bg="#111C33")
        top_metric.pack(fill="x")

        time_container = tk.Frame(top_metric, bg="#111C33")
        time_container.pack(side="left")

        tk.Label(
            time_container,
            text="EXECUTION TIME",
            font=(THEME["font_family"], 8, "bold"),
            fg="#93C5FD",
            bg="#111C33",
        ).pack(anchor="w")

        self.time_label = tk.Label(
            time_container,
            text="⏱ 0.000000 s",
            font=(THEME["font_family"], 19, "bold"),
            fg="#60A5FA",
            bg="#111C33",
        )
        self.time_label.pack(anchor="w")

        chips_frame = tk.Frame(top_metric, bg="#111C33")
        chips_frame.pack(side="right", pady=2)

        self.algo_badge = tk.Label(
            chips_frame,
            text="Algorithm: None",
            font=(THEME["font_family"], 9, "bold"),
            fg="#FFFFFF",
            bg="#3730A3",
            padx=8,
            pady=3,
        )
        self.algo_badge.pack(side="left", padx=3)

        self.complexity_badge = tk.Label(
            chips_frame,
            text="Complexity: -",
            font=(THEME["font_family"], 9, "bold"),
            fg="#FEF3C7",
            bg="#78350F",
            padx=8,
            pady=3,
        )
        self.complexity_badge.pack(side="left", padx=3)

        self.verified_badge = tk.Label(
            chips_frame,
            text="✓ Ready",
            font=(THEME["font_family"], 9, "bold"),
            fg="#D1FAE5",
            bg="#065F46",
            padx=8,
            pady=3,
        )
        self.verified_badge.pack(side="left", padx=3)

    def _parse_input_vector(self):
        raw = self.input_entry.get().strip()
        if not raw:
            raise ValueError("Input list is empty. Please enter numbers.")

        cleaned = raw.replace(",", " ")
        tokens = cleaned.split()
        if not tokens:
            raise ValueError("No valid numbers found in input.")

        numbers = []
        for t in tokens:
            try:
                numbers.append(int(t))
            except ValueError:
                raise ValueError(f"'{t}' is not a valid integer. Please enter integers only.")
        return numbers

    def _set_input_list(self, numbers):
        text = ", ".join(str(x) for x in numbers)
        self.input_entry.delete(0, tk.END)
        self.input_entry.insert(0, text)
        self._on_entry_changed()

    def _clear_input(self):
        self.input_entry.delete(0, tk.END)
        self._on_entry_changed()

    def _generate_nearly_sorted(self):
        arr = list(range(10, 260, 10))
        if len(arr) >= 4:
            arr[2], arr[6] = arr[6], arr[2]
            arr[12], arr[18] = arr[18], arr[12]
        self._set_input_list(arr)

    def _on_entry_changed(self, event=None):
        try:
            vec = self._parse_input_vector()
            self.count_badge.config(text=f"{len(vec)} elements", fg=THEME["text_muted"])
            self.visualizer.update_data(vec, is_sorted=False)
            self.sort_state_label.config(text="Unsorted Input", fg=THEME["text_muted"])
        except ValueError:
            self.count_badge.config(text="Invalid Input", fg=THEME["danger"])
            self.visualizer.update_data([], is_sorted=False)

    def _copy_result_to_clipboard(self):
        if self.last_sorted_result is not None:
            text = ", ".join(str(x) for x in self.last_sorted_result)
            self.clipboard_clear()
            self.clipboard_append(text)
            self.status_badge.config(text="✓ COPIED TO CLIPBOARD", fg="#34D399", bg="#064E3B")
            self.after(2000, lambda: self.status_badge.config(text="● SYSTEM READY", fg=THEME["success"], bg="#064E3B"))

    def run_algorithm(self, algo_name):
        try:
            vector = self._parse_input_vector()
        except ValueError as err:
            messagebox.showerror("Invalid Input", str(err))
            return

        if algo_name not in ALGORITHMS:
            return

        meta = ALGORITHMS[algo_name]
        func = meta["func"]

        sorted_result, exec_time = calculate_execution_time(func, vector, verbose=False)
        self.last_sorted_result = sorted_result
        self.last_execution_time = exec_time
        self.last_algorithm_name = algo_name

        is_correct = sorted_result == sorted(vector)

        self.visualizer.update_data(sorted_result, is_sorted=True)
        self.sort_state_label.config(
            text=f"Sorted by {algo_name} ✓",
            fg=THEME["success"] if is_correct else THEME["danger"],
        )

        res_str = ", ".join(str(x) for x in sorted_result)
        self.result_display.config(state="normal")
        self.result_display.delete(0, tk.END)
        self.result_display.insert(0, res_str)
        self.result_display.config(state="readonly")

        if exec_time < 0.001:
            time_display = f"⏱ {exec_time * 1_000_000:.2f} µs ({exec_time:.6f} s)"
        elif exec_time < 1.0:
            time_display = f"⏱ {exec_time * 1000:.3f} ms ({exec_time:.6f} s)"
        else:
            time_display = f"⏱ {exec_time:.6f} s"

        self.time_label.config(text=time_display, fg="#60A5FA")
        self.algo_badge.config(text=f"Algorithm: {algo_name}")
        self.complexity_badge.config(text=f"Complexity: {meta['complexity']}")
        self.verified_badge.config(
            text="✓ Verified Sorted" if is_correct else "✗ Sort Error",
            fg="#D1FAE5" if is_correct else "#FEE2E2",
            bg="#065F46" if is_correct else "#991B1B",
        )
        self.status_badge.config(
            text=f"● {algo_name.upper()} COMPLETED",
            fg="#34D399",
            bg="#064E3B",
        )

    def run_benchmark_all(self):
        try:
            vector = self._parse_input_vector()
        except ValueError as err:
            messagebox.showerror("Invalid Input", str(err))
            return

        results = []
        for name, meta in ALGORITHMS.items():
            sorted_res, exec_time = calculate_execution_time(meta["func"], vector, verbose=False)
            results.append((name, meta["complexity"], exec_time, sorted_res))

        results.sort(key=lambda x: x[2])
        fastest_name, _, fastest_time, final_sorted = results[0]

        self.last_sorted_result = final_sorted
        self.visualizer.update_data(final_sorted, is_sorted=True)
        self.sort_state_label.config(text="Benchmark Completed ✓", fg=THEME["success"])

        res_str = ", ".join(str(x) for x in final_sorted)
        self.result_display.config(state="normal")
        self.result_display.delete(0, tk.END)
        self.result_display.insert(0, res_str)
        self.result_display.config(state="readonly")

        if fastest_time < 0.001:
            time_display = f"⏱ Fastest: {fastest_name} ({fastest_time * 1_000_000:.2f} µs)"
        else:
            time_display = f"⏱ Fastest: {fastest_name} ({fastest_time * 1000:.3f} ms)"

        self.time_label.config(text=time_display, fg="#34D399")
        self.algo_badge.config(text=f"Fastest: {fastest_name}")
        self.complexity_badge.config(text=f"Benchmark: {len(ALGORITHMS)} Algos")
        self.verified_badge.config(text="✓ All Verified", fg="#D1FAE5", bg="#065F46")

        self._show_benchmark_modal(results, len(vector))

    def _show_benchmark_modal(self, results, n_elements):
        modal = tk.Toplevel(self)
        modal.title(f"Benchmark Results — N = {n_elements} Elements")
        modal.geometry("620x560")
        modal.configure(bg=THEME["bg_root"])
        modal.transient(self)
        modal.grab_set()

        container = tk.Frame(modal, bg=THEME["bg_root"], padx=20, pady=16)
        container.pack(fill="both", expand=True)

        tk.Label(
            container,
            text="🏆 Algorithm Performance Leaderboard",
            font=(THEME["font_family"], 16, "bold"),
            fg=THEME["text_main"],
            bg=THEME["bg_root"],
        ).pack(anchor="w", pady=(0, 4))

        tk.Label(
            container,
            text=f"Tested with {n_elements} elements, ranked from fastest to slowest:",
            font=(THEME["font_family"], 10),
            fg=THEME["text_muted"],
            bg=THEME["bg_root"],
        ).pack(anchor="w", pady=(0, 10))

        for rank, (name, complexity, exec_time, _) in enumerate(results, 1):
            row_card = tk.Frame(
                container,
                bg=THEME["bg_card"],
                highlightthickness=1,
                highlightbackground="#3B82F6" if rank == 1 else THEME["border"],
                padx=10,
                pady=4,
            )
            row_card.pack(fill="x", pady=1)

            rank_label = f"#{rank}" if rank > 3 else ["🥇", "🥈", "🥉"][rank - 1]
            tk.Label(
                row_card,
                text=f"{rank_label}  {name}",
                font=(THEME["font_family"], 10, "bold"),
                fg="#F8FAFC" if rank > 1 else "#38BDF8",
                bg=THEME["bg_card"],
            ).pack(side="left")

            tk.Label(
                row_card,
                text=complexity,
                font=(THEME["font_family"], 8, "bold"),
                fg=THEME["text_muted"],
                bg=THEME["bg_card_inner"],
                padx=6,
                pady=1,
            ).pack(side="left", padx=8)

            if exec_time < 0.001:
                t_str = f"{exec_time * 1_000_000:.2f} µs"
            elif exec_time < 1.0:
                t_str = f"{exec_time * 1000:.3f} ms"
            else:
                t_str = f"{exec_time:.6f} s"

            tk.Label(
                row_card,
                text=t_str,
                font=(THEME["font_family"], 10, "bold"),
                fg="#34D399" if rank == 1 else THEME["text_main"],
                bg=THEME["bg_card"],
            ).pack(side="right")

        close_btn = RoundedCanvasButton(
            container,
            text="Close Leaderboard",
            command=modal.destroy,
            bg_color=THEME["accent_primary"],
            hover_color="#818CF8",
            text_color="#FFFFFF",
            radius=6,
            height=32,
            width=180,
            font_size=10,
            bold=True,
            canvas_bg=THEME["bg_root"],
        )
        close_btn.pack(pady=(12, 0))


def launch_gui(initial_list=None):
    """Entrypoint to start the modern Sorting GUI application."""
    app = SortsApp(initial_list=initial_list)
    app.mainloop()


if __name__ == "__main__":
    launch_gui()
