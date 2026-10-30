import 'package:flutter/material.dart';

/// Five common data-driven UI states to inspect in the visual matrix.
enum QaUiState { loading, content, empty, error, offline }

/// Purposefully ordinary responsive test fixture. It is not an app design
/// system or a replacement for the consuming app's Product Bible.
class QaFixture extends StatelessWidget {
  const QaFixture({
    super.key,
    required this.state,
    this.longLocale = false,
    this.withAdSlot = false,
  });

  final QaUiState state;
  final bool longLocale;
  final bool withAdSlot;

  @override
  Widget build(BuildContext context) {
    final scheme = Theme.of(context).colorScheme;
    final large = MediaQuery.sizeOf(context).width >= 600;
    final headline = longLocale
        ? 'Calendario di attività e promemoria condivisi con descrizioni molto lunghe'
        : 'Your daily overview';

    return Scaffold(
      appBar: AppBar(title: const Text('Visual QA sample')),
      body: SafeArea(
        child: Column(
          children: [
            Expanded(
              child: LayoutBuilder(
                builder: (context, constraints) {
                  final extremeText =
                      MediaQuery.textScalerOf(context).scale(1.0) >= 1.8;
                  final body = Padding(
                    padding: const EdgeInsets.all(16),
                    child: extremeText
                        // Under 200% font scaling, the editorial headline can
                        // occupy most of a small screen. Scroll the content
                        // rather than constraining it to a fixed-height Column.
                        ? ListView(
                            children: [
                              Text(
                                headline,
                                style: Theme.of(context).textTheme.headlineSmall,
                              ),
                              const SizedBox(height: 16),
                              SizedBox(
                                height: 360,
                                child: _content(context),
                              ),
                            ],
                          )
                        : Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                headline,
                                style: Theme.of(context).textTheme.headlineSmall,
                              ),
                              const SizedBox(height: 16),
                              Expanded(child: _content(context)),
                            ],
                          ),
                  );
                  if (!large) return body;
                  return Center(
                    child: ConstrainedBox(
                      constraints: const BoxConstraints(maxWidth: 720),
                      child: body,
                    ),
                  );
                },
              ),
            ),
            if (withAdSlot)
              SizedBox(
                height: 56,
                width: double.infinity,
                child: ColoredBox(
                  color: scheme.surfaceContainerHighest,
                  child: const Center(child: Text('Reserved banner slot')),
                ),
              ),
          ],
        ),
      ),
      bottomNavigationBar:
          MediaQuery.textScalerOf(context).scale(1.0) >= 1.8
              ? SizedBox(
                  height: 72,
                  child: Row(
                    children: [
                      Expanded(
                        child: IconButton(
                          onPressed: () {},
                          tooltip: 'Home',
                          icon: const Icon(Icons.home_outlined),
                        ),
                      ),
                      Expanded(
                        child: IconButton(
                          onPressed: () {},
                          tooltip: 'Diary',
                          icon: const Icon(Icons.calendar_today_outlined),
                        ),
                      ),
                    ],
                  ),
                )
              : NavigationBar(
                  selectedIndex: 0,
                  destinations: const [
                    NavigationDestination(
                      icon: Icon(Icons.home_outlined),
                      label: 'Home',
                    ),
                    NavigationDestination(
                      icon: Icon(Icons.calendar_today_outlined),
                      label: 'Diary',
                    ),
                  ],
                ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {},
        tooltip: 'Add entry',
        child: const Icon(Icons.add),
      ),
    );
  }

  Widget _content(BuildContext context) {
    switch (state) {
      case QaUiState.loading:
        return const Center(child: CircularProgressIndicator.adaptive());
      case QaUiState.empty:
        return _Message(
          icon: Icons.inbox_outlined,
          headline: 'Nothing here yet',
          detail: 'Create your first item using the action button.',
        );
      case QaUiState.error:
        return _Message(
          icon: Icons.error_outline,
          headline: 'Unable to load',
          detail: 'Check connectivity and try again.',
        );
      case QaUiState.offline:
        return _Message(
          icon: Icons.cloud_off_outlined,
          headline: 'Working offline',
          detail: 'Your saved items remain available.',
        );
      case QaUiState.content:
        return ListView(
          children: const [
            ListTile(
              leading: Icon(Icons.check_circle_outline),
              title: Text('First saved item'),
              subtitle: Text('Today at 10:00'),
            ),
            ListTile(
              leading: Icon(Icons.bookmark_outline),
              title: Text('An item with a longer, variable-length subtitle'),
              subtitle: Text('Future reminders and notes'),
            ),
          ],
        );
    }
  }
}

class _Message extends StatelessWidget {
  const _Message({
    required this.icon,
    required this.headline,
    required this.detail,
  });

  final IconData icon;
  final String headline;
  final String detail;

  @override
  Widget build(BuildContext context) => Center(
        child: SingleChildScrollView(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Icon(icon, size: 44),
              const SizedBox(height: 12),
              Text(headline,
                  textAlign: TextAlign.center,
                  style: Theme.of(context).textTheme.titleMedium),
              const SizedBox(height: 8),
              Text(detail, textAlign: TextAlign.center),
              const SizedBox(height: 16),
              OutlinedButton(
                onPressed: () {},
                child: const Text('Try again'),
              ),
            ],
          ),
        ),
      );
}
