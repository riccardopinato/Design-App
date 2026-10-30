import 'package:factory_visual_qa/factory_visual_qa.dart';
import 'package:flutter/material.dart';

void main() => runApp(const VisualQaShowcase());

/// Full-window QA demo. Settings use an overlay menu, never a stacked column
/// that shrinks the actual screen under test on short landscape devices.
class VisualQaShowcase extends StatefulWidget {
  const VisualQaShowcase({super.key});

  @override
  State<VisualQaShowcase> createState() => _VisualQaShowcaseState();
}

class _VisualQaShowcaseState extends State<VisualQaShowcase> {
  bool dark = false;
  bool adSlot = false;
  bool longLocale = false;
  QaUiState state = QaUiState.content;

  @override
  Widget build(BuildContext context) => MaterialApp(
        debugShowCheckedModeBanner: false,
        title: 'Factory Visual QA',
        theme: ThemeData(useMaterial3: true, colorSchemeSeed: Colors.indigo),
        darkTheme: ThemeData(
          useMaterial3: true,
          colorScheme: ColorScheme.fromSeed(
            seedColor: Colors.indigo,
            brightness: Brightness.dark,
          ),
        ),
        themeMode: dark ? ThemeMode.dark : ThemeMode.light,
        home: Stack(
          children: [
            QaFixture(
              state: state,
              withAdSlot: adSlot,
              longLocale: longLocale,
            ),
            Positioned(
              top: 2,
              right: 8,
              child: SafeArea(
                child: Material(
                  color: Colors.transparent,
                  child: PopupMenuButton<String>(
                    tooltip: 'QA preview options',
                    icon: const Icon(Icons.tune),
                    onSelected: (choice) => setState(() {
                      switch (choice) {
                        case 'dark':
                          dark = !dark;
                        case 'banner':
                          adSlot = !adSlot;
                        case 'locale':
                          longLocale = !longLocale;
                        default:
                          if (choice.startsWith('state:')) {
                            state = QaUiState.values.byName(
                              choice.substring('state:'.length),
                            );
                          }
                      }
                    }),
                    itemBuilder: (context) => [
                      CheckedPopupMenuItem(
                        value: 'dark',
                        checked: dark,
                        child: const Text('Dark theme'),
                      ),
                      CheckedPopupMenuItem(
                        value: 'banner',
                        checked: adSlot,
                        child: const Text('Banner slot'),
                      ),
                      CheckedPopupMenuItem(
                        value: 'locale',
                        checked: longLocale,
                        child: const Text('Long localization'),
                      ),
                      const PopupMenuDivider(),
                      for (final option in QaUiState.values)
                        CheckedPopupMenuItem(
                          value: 'state:${option.name}',
                          checked: option == state,
                          child: Text(option.name),
                        ),
                    ],
                  ),
                ),
              ),
            ),
          ],
        ),
      );
}
